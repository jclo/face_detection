# ******************************************************************************
"""
Implements Haarcascades and dlib techniques to detect faces on image or video.


Private Functions:
    . _parse                    parses the script arguments,
    . _process_image            decodes faces on an image,
    . _process_video            decodes faces on a video,


Public:
    . main                      starts the script


@namespace      _
@author         <author_name>
@since          0.0.0
@version        0.0.0
@licence        MIT. Copyright (c) 2020 Mobilabs <contact@mobilabs.fr>
"""
# ******************************************************************************
import argparse
import cv2
from decoders.dlib import Dlib
from decoders.haar import Haar


HAAR_FRONTFACE = './resources/haarcascades/haarcascade_frontalface_default.xml'
RECT_COLOR = (0, 255, 255)
RECT_THICKNESS = 2
VIDEO_SCALE = 0.5


# -- Private Functions ---------------------------------------------------------

def _parse():
    """Parses the script arguments.

    ### Parameters:
        param1 ():          none,

    ### Returns:
        (str):              returns the option values,

    ### Raises:
        none
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--operation', type=str, help='get or show image/video')
    parser.add_argument('-t', '--type', type=str, help='extract or detect face')
    parser.add_argument('-m', '--method', type=str, help='haarcascades or dlib')
    parser.add_argument('-s', '--source', type=str, help='path of the input image or video')
    parser.add_argument('-d', '--destination', type=str, help='path of the output image or video')
    args = parser.parse_args()

    if args.operation is None or args.type is None or args.method is None \
       or args.source is None or args.destination is None:
        print('You must define all the parameters!')
        parser.print_help()
        exit()
    else:
        return args.operation, args.type, args.method, args.source, args.destination


def _process_image(op, type, method, source, dest):
    """Subroutine to process an image."""
    if op == 'get':
        if type == 'extract':
            print('Extract face with ' + method)
            cv2.imwrite(dest, detector.get_face(cv2.imread(source)))

        elif type == 'detect':
            print('Detects face(s) with ' + method)
            cv2.imwrite(dest, detector.get_image_with_faces(cv2.imread(source)))
        else:
            print('the option --type must be get or detect')
            exit()

    elif op == 'show':
        if type == 'extract':
            print('Extract face with ' + method)
            cv2.imshow('Extracted Face', detector.get_face(cv2.imread(source)))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif type == 'detect':
            print('Detects face(s) with ' + method)
            cv2.imshow('Detected Face(s)', detector.get_image_with_faces(cv2.imread(source)))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print('the option --type must be get or detect')
            exit()

    else:
        print('Unrecognized request!')
        exit()


def _process_video(op, type, method, source, dest):
    """Subroutine to process a video."""
    if op == 'get':
        if type == 'extract':
            print('This option is not supported for videos!')

        elif type == 'detect':
            print('Detects face(s) with ' + method + ' - push the enter key to exit')
            cap = cv2.VideoCapture(source)
            frame_width = int(cap.get(3) * VIDEO_SCALE)
            frame_height = int(cap.get(4) * VIDEO_SCALE)
            out = cv2.VideoWriter(d, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

            while(True):
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=VIDEO_SCALE, fy=VIDEO_SCALE, interpolation=cv2.INTER_LINEAR)
                mod_frame = detector.get_image_with_faces(frame)
                out.write(mod_frame)
                cv2.imshow('Face Detection', mod_frame)
                if cv2.waitKey(1) == 13:
                    break

            cap.release()
            out.release()
            cv2.destroyAllWindows()

        else:
            print('the option --type must be get or detect')
            exit()

    elif op == 'show':
        if type == 'extract':
            print('This option is not supported for videos!')

        elif type == 'detect':
            print('Detects face(s) with ' + method + ' - push the enter key to exit')
            # Open the video file
            cap = cv2.VideoCapture(source)

            # Read the video frame by frame
            while(True):
                ret, frame = cap.read()
                frame = cv2.resize(frame, None, fx=VIDEO_SCALE, fy=VIDEO_SCALE, interpolation=cv2.INTER_LINEAR)
                mod_frame = detector.get_image_with_faces(frame)
                cv2.imshow('Face Detection', mod_frame)
                # exit if the enter key is pushed
                # To speed up or slow down the video rate, change the delay
                # passed-in argument to waitKey().
                if cv2.waitKey(1) == 13:
                    break
            cap.release()
            cv2.destroyAllWindows()

        else:
            print('the option --type must be extract or detect')
            exit()

    else:
        print('Unrecognized request!')
        exit()


# -- Public Functions ----------------------------------------------------------

if __name__ == '__main__':

    o, t, m, s, d = _parse()

    if m == 'haarcascades':
        detector = Haar()
    elif m == 'dlib':
        detector = Dlib()
    else:
        print('The detection method must be haarcascades or dlib!')
        exit()

    if s.endswith('jpg') or s.endswith('png'):
        _process_image(o, t, m, s, d)
    elif s.endswith('mp4'):
        _process_video(o, t, m, s, d)
    else:
        print('The source file is unknown!')
        exit()

# -- o ---
