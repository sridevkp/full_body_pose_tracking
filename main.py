import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic


BG_COLOR = (192, 192, 192)

cap = cv.VideoCapture(0)

with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:
    while True:
        ret, frame = cap.read()
        if not ret : continue
        w, h, _ = frame.shape

        img = cv.cvtColor( frame, cv.COLOR_BGR2RGB )
        results = holistic.process( img )
        if results.pose_landmarks:
            nose = results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE]
            eyes = results.pose_landmarks.landmark[mp_holistic.PoseLandmrk.NOSE]
            # cv.circle( frame, ( int(nose.x *w), int(nose.y *h) ), 5, 255, 1 )
            
            # mp_drawing.draw_landmarks( 
            #     frame,
            #     results.face_landmarks,
            #     mp_holistic.FACEMESH_CONTOURS,
            #     landmark_drawing_spec=None,
            #     connection_drawing_spec=mp_drawing_styles
            #     .get_default_face_mesh_contours_style())
            
            mp_drawing.draw_landmarks(
                frame,
                results.face_landmarks,
                mp_holistic.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())
                    
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles
                .get_default_pose_landmarks_style())
            
        cv.imshow( "main", frame )
        if cv.waitKey(1) == ord("q"): break 

cap.release()
cv.destroyAllWindows()