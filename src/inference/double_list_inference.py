from itertools import accumulate, chain


def flatten(inputs):
    """Flatten a double list.

    Args:
        inputs (list): A double list.

    Returns:
        list: A single list.

    Examples:
        >>> inputs = [[1, 2, 3], [4, 5, 6]]
        >>> flatten(inputs)
        >>> [1, 2, 3, 4, 5, 6]
    """
    return list(chain.from_iterable(inputs))


def deflatten(inputs, num_items):
    """Deflatten a single list to a double list.

    Args:
        inputs (list): A single list.
        num_items (list): A list of the number of items in each sub-list.

    Returns:
        list: A double list.

    Examples:
        >>> inputs = [1, 2, 3, 4, 5, 6]
        >>> item_indices = [0, 0, 0, 1, 1, 1]
        >>> deflatten(inputs, item_indices)
        >>> [[1, 2, 3], [4, 5, 6]]
    """
    num_items = [0] + list(accumulate(num_items))
    outputs = []
    for i in range(len(num_items) - 1):
        outputs.append(inputs[num_items[i]:num_items[i + 1]])
    return outputs


def inference_double_list(inputs, inference_func, *args, **kwargs):
    """Inference a double list of inputs with a function, which can be applied to a single list.

    Args:
        inputs (list): A double list of inputs.
        inference_func (function): A function to inference a single list.

    Returns:
        list: A double list of inference results with the same shape as inputs.

    Examples:
        >>> inputs = [[1, 2, 3], [4, 5, 6]]
        >>> inference_func = lambda x: [i**2 for i in x]
        >>> inference_double_list(inputs, inference_func)
        >>> [[1, 4, 9], [16, 25, 36]]
    """
    num_items = [len(i) for i in inputs]
    inputs = flatten(inputs)
    outputs = inference_func(inputs, *args, **kwargs)
    outputs = deflatten(outputs, num_items)
    return outputs


if __name__ == '__main__':
    inputs = [[1, 2, 3], [4, 5, 6]]
    def inference_func(x): return [i**2 for i in x]
    print('expected', [[1, 4, 9], [16, 25, 36]])
    print('outputs', inference_double_list(inputs, inference_func))

    def inference_func(x): return [[i * 2, i * 3] for i in x]

    print('expected', [[[2, 3], [4, 6], [6, 9]], [[8, 12], [10, 15], [12, 18]]])
    print('outputs', inference_double_list(inputs, inference_func))
