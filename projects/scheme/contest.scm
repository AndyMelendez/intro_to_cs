;;; Scheme Recursive Art Contest Entry
;;;
;;; cs61a-wh & cs61a-akz
;;;
;;; Title: You Know What It Is: Black & Yellow
;;;
;;; Description/Haiku:
;;;    Hilbert's space-filler
;;;    Fills Mandelbrot set. Outside,
;;;    A coloring scheme.


(speed 99999)

(define side 1)
(define ang 91)
(speed 9999999)
(forward 1000)
(left 90)
(begin_fill)
(circle 1000)
(end_fill)

(define (spiral increment angle iterations)
  (define (drawer i) 
    (cond ((= i iterations) '())
	  (else (begin (fd (* i increment)) (lt angle) (drawer (+ i 1))))
    )
  )
        (drawer 0)
)

(define (draw)
  (begin (
	  (setpos 0 0)
      (color 'yellow)
      (spiral 0.45 93 890)
      (penup)
      (setpos 0 0)
      (pendown)
      (color 'black)
	  (spiral 0.35 93 850)
      (penup)
      (setpos 0 0)
      (pendown)
      (color 'darkgreen)
      (spiral 0.45 93 600)
      (penup)
      (setpos 0 0)
      (pendown)
      (color 'black)
	  (spiral 0.45 93 500)
	  )
  )
)



(draw)
(hideturtle)
;(exitonclick)
