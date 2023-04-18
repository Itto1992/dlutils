def batch_generator(iterable, batch_size):
    """Batch generator.

    Args:
        iterable (Iterable): Iterable object.
        batch_size (int): batch size.

    Examples:
        >>> inputs = [img, img, ..., img]  # long list of images
        >>> outputs = []
        >>> for batch in batch_generator(inputs, 8):
        >>>     _outputs = model(batch)  # inference with batch_size is 8
        >>>     outputs.extend(_outputs)
    """
    start = 0
    while start < len(iterable):
        end = start + batch_size
        yield iterable[start:end]
        start = end


def batch_inference(inputs, func, *args, **kwargs):
    """Batch inference.

    Args:
        inputs (list): List of inputs.
        func (Callable): Function to apply inference.

    Returns:
        list: List of outputs.
    """
    outputs = []
    for batch in batch_generator(inputs, 8):
        outputs.extend(func(batch, *args, **kwargs))
    return outputs
