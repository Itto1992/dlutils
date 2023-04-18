import os
import unittest
from pathlib import Path

from src.video import video_generator

VIDEO_PATH = '/.cache/test.mp4'
VIDEO_HEIGHT = 1080
VIDEO_WIDTH = 1920
VIDEO_LENGTH = 171


class TestVideoGenerator(unittest.TestCase):

    def setUp(self):
        if not Path(VIDEO_PATH).parent.exists():
            Path(VIDEO_PATH).parent.mkdir(parents=True)
            os.system(f'wget -O {VIDEO_PATH} https://download.samplelib.com/mp4/sample-5s.mp4')

    def test_video_generator(self):
        test_cases = [
            # (batch_size, start_frame, end_frame)
            (1, 0, None),
            (8, 0, None),
            (8, 0, 100),
            (8, 100, 150),
        ]
        for case in test_cases:
            with self.subTest(case=case):
                batch_size, start_frame, end_frame = case
                num_frames = 0
                video_length = end_frame - start_frame if end_frame is not None else VIDEO_LENGTH
                for batch in video_generator(VIDEO_PATH, batch_size, start_frame, end_frame):
                    if len(batch) != batch_size:
                        self.assertEqual(num_frames + len(batch), video_length)
                    for frame in batch:
                        self.assertEqual(frame.shape, (VIDEO_HEIGHT, VIDEO_WIDTH, 3))
                    num_frames += len(batch)


if __name__ == '__main__':
    unittest.main()
