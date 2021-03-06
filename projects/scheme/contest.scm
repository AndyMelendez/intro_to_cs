;;; Scheme Recursive Art Contest Entry
;;;
;;; cs61a-wh & cs61a-akz
;;;
;;; Title: You Know What It Is: Black & Yellow
;;;
;;; Description/Haiku:
;;;    Reaching for heaven,
;;;    Getting closer to the Sun,
;;;    Like a Sunflower.
;;;
;;; Time to Complete: 2:25 or 145 seconds

(speed 0)

;; Creates Black Background
(define side 1)
(define ang 91)
(speed 9999999)
(forward 1000)
(left 90)
(begin_fill)
(color 'black)
(circle 1000)
(end_fill)

;; Executes Spirals
(define (spiral increment angle iterations)
  (define (drawer i) 
    (cond ((= i iterations) '())
	  (else (begin (fd (* i increment)) (lt angle) (drawer (+ i 1))))
    )
  )
        (drawer 0)
)

;; Dictates Drawing
(define (draw)
  (begin (
	  (setpos 0 0)
      (color 'yellow)
      (spiral 0.45 93 875)
      (penup)
      (setpos 0 0)
      (pendown)
      (color 'darkgreen)
	  (spiral 0.35 93 660)
      (penup)
      (setpos 0 0)
      (pendown)
      (color 'black)
	  (spiral 0.35 93 600)
      (penup)
      (setpos 0 0)
      (pendown)
      (color 'orange)
      (spiral 0.60 93 180)
      (penup)
      (setpos 0 0)
      (pendown)
      (color 'black)
	  (spiral 0.25 93 450)
	  )
  )
)

(draw)
(hideturtle)
;(exitonclick)
