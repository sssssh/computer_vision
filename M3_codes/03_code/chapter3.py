#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""OpenCV with Python Blueprints
    Chapter 3: Finding Objects Via Feature Matching and Perspective Transforms

    An app to detect and track an object of interest in the video stream of a
    webcam, even if the object is viewed at different angles, distances, or
    under partial occlusion.
"""

import cv2
import wx

from gui import BaseLayout
from feature_matching import FeatureMatching


class FeatureMatchingLayout(BaseLayout):
    """A custom layout for feature matching display

        A plain GUI layout for feature matching output.
        Each captured frame is passed to the FeatureMatching class, so that an
        object of interest can be tracked.
    """
    def _init_custom_layout(self):
        """Initializes feature matching class"""
        self.matching = FeatureMatching(train_image='salinger.jpg')

    def _create_custom_layout(self):
        """Use plain layout"""
        pass

    def _process_frame(self, frame):
        """Processes each captured frame"""
        # if object detected, display new frame, else old one
        success, new_frame = self.matching.match(frame)
        if success:
            return new_frame
        else:
            return frame


def main():
    capture = cv2.VideoCapture(0)
    if not(capture.isOpened()):
        capture.open()

    capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    # start graphical user interface
    app = wx.App()
    layout = FeatureMatchingLayout(None, -1, 'Feature Matching', capture)
    layout.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
