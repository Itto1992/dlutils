from pathlib import Path

import cv2


def video_generator(video, batch_size=1, start_frame=0, end_frame=None):
    """Convert video path or VideoCapture instance to a generator of RGB images.

    Args:
        video (str or Path or cv2.VideoCapture): Video path or VideoCapture instance.
        batch_size (int): Batchsize.
            default = 1
        start_frame (int): Start frame.
            default = 0
        end_frame (int): End frame. Note that this is not included in the output.
                If None, the video is read until the end.
            default = None

    Returns:
        (List[numpy.ndarray]): A list of arrays of RGB images.

    Examples:
        >>> video_path = 'path/to/video'
        >>> outputs = []
        >>> for batch in video_generator(video_path, batchsize):
        >>>     outputs.extend(model(batch))
    """
    if isinstance(video, (str, Path)):
        video = cv2.VideoCapture(str(video))
    elif not isinstance(video, cv2.VideoCapture):
        raise ValueError('`video` must be video path or cv2.VideoCapture instance.')

    # set start frame
    video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    batch = []
    current_frame = start_frame
    while video.isOpened():
        success, frame = video.read()

        if not success or (end_frame is not None and current_frame >= end_frame):
            if len(batch):
                yield batch
            break

        batch.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if len(batch) == batch_size:
            yield batch
            batch = []

        current_frame += 1

    video.release()
