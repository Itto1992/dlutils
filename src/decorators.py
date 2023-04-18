from functools import wraps

from .inference import batch_inference, inference_double_list


def doublelistify(func):
    @wraps(func)
    def wrapper(inputs, *args, **kwargs):
        return inference_double_list(inputs, func, *args, **kwargs)
    return wrapper


def batchify(func):
    @wraps(func)
    def wrapper(inputs, *args, **kwargs):
        return batch_inference(inputs, func, *args, **kwargs)
    return wrapper


if __name__ == '__main__':
    def inference_single_list(inputs):
        return [x * 2 for x in inputs]

    @doublelistify
    def _inference_double_list(inputs):
        return inference_single_list(inputs)

    inputs = [list(range(3)) for _ in range(3)]
    print('expected', [[x * 2 for x in inputs] for inputs in inputs])
    print('outputs', _inference_double_list(inputs))
