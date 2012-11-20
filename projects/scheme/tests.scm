;;; Test cases for Scheme.
;;;
;;; In order to run only a prefix of these examples, add the line
;;;
;;; (exit)
;;;
;;; after the last test you wish to run.

;;; *** Add more of your own here! ***

;;; These are examples from several sections of "The Structure
;;; and Interpretation of Computer Programs" by Abelson and Sussman.

;;; License: Creative Commons share alike with attribution

;;; 1.1.1

10
; expect 10

(+ 137 349)
; expect 486

(- 1000 334)
; expect 666

(* 5 99)
; expect 495

(/ 10 5)
; expect 2

(+ 2.7 10)
; expect 12.7

(+ 21 35 12 7)
; expect 75

(* 25 4 12)
; expect 1200

(+ (* 3 5) (- 10 6))
; expect 19

(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))
; expect 57

(+ (* 3
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7)
      6))
; expect 57


'(1 2 3)
; expect (1 2 3)

'('a 2 3)
; expect ((quote a) 2 3)

'hoy
; expect hoy


;;; 1.1.2

(define size 2)
size
; expect 2

(* 5 size)
; expect 10

(define pi 3.14159)
(define radius 10)
(* pi (* radius radius))
; expect 314.159

(define circumference (* 2 pi radius))
circumference
; expect 62.8318

;;; More additional tests

(define hub 123)
(define tab 100)
(* hub (* tab tab))
; expect 1230000

(define pounds 23)
(define kilo-constant 0.453592)
(* pounds kilo-constant)
; expect 10.432616

(define nothing 10)
(define something 100)
(* nothing (* something (/ something nothing)))
; expect 10000
 
;;; 1.1.4

(define (square x) (* x x))
(square 21)
; expect 441

(define square (lambda (x) (* x x))) ; See Section 1.3.2
(square 21)
; expect 441

(square (+ 2 5))
; expect 49

(square (square 3))
; expect 81

(define (sum-of-squares x y)
  (+ (square x) (square y)))
(sum-of-squares 3 4)
; expect 25

(define (f a)
  (sum-of-squares (+ a 1) (* a 2)))
(f 5)
; expect 136

(define x-cubing (lambda (x) (* x x x )))
(x-cubing 23)
; expect 12167
 
(define y-cubing (lambda (y) (* y y y)))
(y-cubing 23)
; expect 12167
 
(define y_sum (lambda (y) (+ y 3)))
(y_sum 4)
; expect 7
 
(define (cubing-sum a b)
    ( + (x-cubing a) (y-cubing b)))
(cubing-sum 1 2)
; expect 9
 
;;; 1.1.6

(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))
(abs -3)
; expect 3

(abs 0)
; expect 0

(abs 3)
; expect 3

(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))
(a-plus-abs-b 3 -2)
; expect 5

(define (du-mar x y)
   ((if (< y 1) - *) x y))
(du-mar -3 1)
; expect -3

(define (oulalala x y z)
   ((if (> (* x y) x) * /) x z))
(oulalala 1 2 3)
; expect 3

;;; 1.1.7

(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x)
                 x)))
(define (improve guess x)
  (average guess (/ x guess)))
(define (average x y)
  (/ (+ x y) 2))
(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))
(define (sqrt x)
  (sqrt-iter 1.0 x))
(sqrt 9)
; expect 3.00009155413138

(sqrt (+ 100 37))
; expect 11.704699917758145

(sqrt (+ (sqrt 2) (sqrt 3)))
; expect 1.7739279023207892

(square (sqrt 1000))
; expect 1000.000369924366

(sqrt (- 140 20))
; expect 10.954451151558928

(square (sqrt 120)) 
; expect 120.00000003189072

(sqrt ( + 80 7))
; expect 9.32739845997726

(square (sqrt 87))
; expect 87.00036203118617

(sqrt 23)
; expect 4.795844112917605

;;; 1.1.8

(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0))
(sqrt 9)
; expect 3.00009155413138

(sqrt (+ 100 37))
; expect 11.704699917758145

(sqrt (+ (sqrt 2) (sqrt 3)))
; expect 1.7739279023207892

(square (sqrt 1000))
; expect 1000.000369924366

(sqrt (- 140 20))
; expect 10.954451151558928

(square (sqrt 120)) 
; expect 120.00000003189072

(sqrt ( + 80 7))
; expect 9.32739845997726

(square (sqrt 87))
; expect 87.00036203118617

(sqrt 23)
; expect 4.795844112917605

;;; 1.3.1

(define (cube x) (* x x x))
(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))
(define (inc n) (+ n 1))
(define (sum-cubes a b)
  (sum cube a inc b))
(sum-cubes 1 10)
; expect 3025

(define (identity x) x)
(define (sum-integers a b)
  (sum identity a inc b))
(sum-integers 1 10)
; expect 55

;;; 1.3.2

((lambda (x y z) (+ x y (square z))) 1 2 3)
; expect 12

(define (f x y)
  (let ((a (+ 1 (* x y)))
        (b (- 1 y)))
    (+ (* x (square a))
       (* y b)
       (* a b))))
(f 3 4)
; expect 456

(define x 5)
(+ (let ((x 3))
     (+ x (* x 10)))
   x)
; expect 38

(let ((x 3)
      (y (+ x 2)))
  (* x y))
; expect 21

(define x 4)
(let ((x 4)
      (y (+ x 2)))
  (* x y))
; expect 24
   
(define ix 1)
(define x 0)
(+ (let ((ix 3))
     (+ x (* ix 10)))
   ix)
; expect 31

(define y 15)
(+ (let ((y 1))
     (+ y (* y 1)))
   y)
; expect 17

((lambda (a b c) (+ a b (sqrt c))) 1 2 3)
; expect 4.732142857142858

(define x 0)
(let ((x 2)
      (y (+ x 2)))
  (* x y))
; expect 4

;;; 2.1.1

(define (add-rat x y)
  (make-rat (+ (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))
(define (sub-rat x y)
  (make-rat (- (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))
(define (mul-rat x y)
  (make-rat (* (numer x) (numer y))
            (* (denom x) (denom y))))
(define (div-rat x y)
  (make-rat (* (numer x) (denom y))
            (* (denom x) (numer y))))
(define (equal-rat? x y)
  (= (* (numer x) (denom y))
     (* (numer y) (denom x))))

(define x (cons 1 2))
(car x)
; expect 1

(cdr x)
; expect 2

(define x (cons 1 2))
(define y (cons 3 4))
(define z (cons x y))
(car (car z))
; expect 1

(car (cdr z))
; expect 3

z
; expect ((1 . 2) 3 . 4)

(define (make-rat n d) (cons n d))
(define (numer x) (car x))
(define (denom x) (cdr x))
(define (print-rat x)
  (display (numer x))
  (display '/)
  (display (denom x))
  (newline))
(define one-half (make-rat 1 2))
(print-rat one-half)
; expect 1/2

(define one-third (make-rat 1 3))
(print-rat (add-rat one-half one-third))
; expect 5/6

(print-rat (mul-rat one-half one-third))
; expect 1/6

(print-rat (add-rat one-third one-third))
; expect 6/9

(define (gcd a b)
  (if (= b 0)
      a
      (gcd b (remainder a b))))
(define (make-rat n d)
  (let ((g (gcd n d)))
    (cons (/ n g) (/ d g))))
(print-rat (add-rat one-third one-third))
; expect 2/3

(define one-through-four (list 1 2 3 4))
one-through-four
; expect (1 2 3 4)

(car one-through-four)
; expect 1

(cdr one-through-four)
; expect (2 3 4)

(car (cdr one-through-four))
; expect 2

(cons 10 one-through-four)
; expect (10 1 2 3 4)

(cons 5 one-through-four)
; expect (5 1 2 3 4)

(define (map proc items)
  (if (null? items)
      nil
      (cons (proc (car items))
            (map proc (cdr items)))))
(map abs (list -10 2.5 -11.6 17))
; expect (10 2.5 11.6 17)

(map (lambda (x) (* x x))
     (list 1 2 3 4))
; expect (1 4 9 16)

(define (scale-list items factor)
  (map (lambda (x) (* x factor))
       items))
(scale-list (list 1 2 3 4 5) 10)
; expect (10 20 30 40 50)

(define (count-leaves x)
  (cond ((null? x) 0)
        ((not (pair? x)) 1)
        (else (+ (count-leaves (car x))
                 (count-leaves (cdr x))))))
(define x (cons (list 1 2) (list 3 4)))
(count-leaves x)
; expect 4

(count-leaves (list x x))
; expect 8

(* (count-leaves (list x x)) 3)
; expect 24

(count-leaves (list x x x))
; expect 12

(map abs (list -1 -2.1 11.9 18))
; expect (1 2.1 11.9 18)

(define two-through (list 2 3.4 1 4.4))
two-through
; expect (2 3.4 1 4.4)

(car two-through)
; expect 2

;;; 2.2.3

(define (odd? x) (= 1 (remainder x 2)))
(define (filter predicate sequence)
  (cond ((null? sequence) nil)
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))
(filter odd? (list 1 2 3 4 5))
; expect (1 3 5)

(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
(accumulate + 0 (list 1 2 3 4 5))
; expect 15

(accumulate * 1 (list 1 2 3 4 5))
; expect 120

(accumulate cons nil (list 1 2 3 4 5))
; expect (1 2 3 4 5)

(define (enumerate-interval low high)
  (if (> low high)
      nil
      (cons low (enumerate-interval (+ low 1) high))))
(enumerate-interval 2 7)
; expect (2 3 4 5 6 7)

(define (enumerate-tree tree)
  (cond ((null? tree) nil)
        ((not (pair? tree)) (list tree))
        (else (append (enumerate-tree (car tree))
                      (enumerate-tree (cdr tree))))))
(enumerate-tree (list 1 (list 2 (list 3 4)) 5))
; expect (1 2 3 4 5)

(filter odd? (list 1 3 7 2 4))
; expect (1 3 7)

(accumulate + 0 (list 1 5 10 20 5))
; expect 41

(enumerate-interval 1 10)
; expect (1 2 3 4 5 6 7 8 9 10)

(accumulate cons nil (list 2 3 4 5))
; expect (2 3 4 5)

(enumerate-tree (list 4 (list 6 (list 7 8)) 10))
; expect (4 6 7 8 10)

;;; 2.3.1

(define a 1)

(define b 2)

(list a b)
; expect (1 2)

(list 'a 'b)
; expect (a b)

(list 'a b)
; expect (a 2)

(car '(a b c))
; expect a

(cdr '(a b c))
; expect (b c)

(define (memq item x)
  (cond ((null? x) false)
        ((eq? item (car x)) x)
        (else (memq item (cdr x)))))
(memq 'apple '(pear banana prune))
; expect False

(memq 'apple '(x (apple sauce) y apple pear))
; expect (apple pear)

(define (equal? x y)
  (cond ((pair? x) (and (pair? y)
                        (equal? (car x) (car y))
                        (equal? (cdr x) (cdr y))))
        ((null? x) (null? y))
        (else (eq? x y))))
(equal? '(1 2 (three)) '(1 2 (three)))
; expect True

(equal? '(1 2 (three)) '(1 2 three))
; expect False

(equal? '(1 2 three) '(1 2 (three)))
; expect False

;;; Peter Norvig tests (http://norvig.com/lispy2.html)

(define double (lambda (x) (* 2 x)))
(double 5)
; expect 10

(define compose (lambda (f g) (lambda (x) (f (g x)))))
((compose list double) 5)
; expect (10)

(define apply-twice (lambda (f) (compose f f)))
((apply-twice double) 5)
; expect 20

((apply-twice (apply-twice double)) 5)
; expect 80

(define fact (lambda (n) (if (<= n 1) 1 (* n (fact (- n 1))))))
(fact 3)
; expect 6

(fact 50)
; expect 30414093201713378043612608166064768844377641568960512000000000000

(define (combine f)
  (lambda (x y)
    (if (null? x) nil
      (f (list (car x) (car y))
         ((combine f) (cdr x) (cdr y))))))
(define zip (combine cons))
(zip (list 1 2 3 4) (list 5 6 7 8))
; expect ((1 5) (2 6) (3 7) (4 8))

(define riff-shuffle (lambda (deck) (begin
    (define take (lambda (n seq) (if (<= n 0) (quote ()) (cons (car seq) (take (- n 1) (cdr seq))))))
    (define drop (lambda (n seq) (if (<= n 0) seq (drop (- n 1) (cdr seq)))))
    (define mid (lambda (seq) (/ (length seq) 2)))
    ((combine append) (take (mid deck) deck) (drop (mid deck) deck)))))
(riff-shuffle (list 1 2 3 4 5 6 7 8))
; expect (1 5 2 6 3 7 4 8)

((apply-twice riff-shuffle) (list 1 2 3 4 5 6 7 8))
; expect (1 3 5 7 2 4 6 8)

(riff-shuffle (riff-shuffle (riff-shuffle (list 1 2 3 4 5 6 7 8))))
; expect (1 2 3 4 5 6 7 8)

(riff-shuffle (list 2 3 7 8 9 10 11 18))
; expect (2 9 3 10 7 11 8 18)

((apply-twice riff-shuffle) (list 2 3 7 8 9 10 11 18))
; expect (2 7 9 11 3 8 10 18)

(zip (list 2 3 8 4) (list 1 9 2 8))
; expect ((2 1) (3 9) (8 2) (4 8))

(fact 20)
; expect 2432902008176640000

(equal? '(1 2 (two)) '(1 2 (two)))
; expect True

(memq 'soda '(pear banana prune))
; expect False

;;; Additional tests

(apply square '(2))
; expect 4

(apply + '(1 2 3 4))
; expect 10

(apply (if false + append) '((1 2) (3 4)))
; expect (1 2 3 4)

(if 0 1 2)
; expect 1

(if '() 1 2)
; expect 1

(or false true)
; expect True

(or)
; expect False

(and)
; expect True

(or 1 2 3)
; expect 1

(and 1 2 3)
; expect 3

(if nil 1 2)
; expect 1

(if 0 1 2)
; expect 1

(if (or false False #f) 1 2)
; expect 2

(define (loop) (loop))
(cond (false (loop))
      (12))
; expect 12

((lambda (x) (display x) (newline) x) 2)
; expect 2
; expect 2

(define g (mu () x))
(define (high f x)
  (f))

(high g 2)
; expect 2

(define (print-and-square x)
  (print x)
  (square x))
(print-and-square 12)
; expect 12
; expect 144

(/ 1 0)
; expect Error

(define addx (mu (x) (+ x y)))
(define add2xy (lambda (x y) (addx (+ x x))))
(add2xy 3 7)
; expect 13

(define add_o (mu (o) (+ o y)))
(define add2_oy (lambda (o y) (add_o (+ o o))))
(add2_oy 4 5)
; expect 13

(define (print-and-square x)
  (print x)
  (square x))
(print-and-square 9)
; expect 9
; expect 81

(and 1 2 4)
; expect 4

(if '() 19 2)
; expect 19

(if nil 87 12)
; expect 87

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Scheme Implementations ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; len outputs the length of list s
(define (len s)
  (if (eq? s '())
    0
    (+ 1 (len (cdr s)))))
(len '(1 2 3 4))
; expect 4
(len '(1 2 3))
; expect 3

; Problem 18

;; Merge two lists LIST1 and LIST2 and returns
;; the merged lists.
(define (merge list1 list2)
    (cond ((null? list1) list2)
          ((null? list2) list1)
          ((< (car list1) (car list2)) (cons (car list1) 
              (merge (cdr list1) list2)))
          (else (cons (car list2) 
              (merge (cdr list2) list1)))))

(merge '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)

(merge '(1 3 5 7) '(1 4 8))
; expect (1 1 3 4 5 7 8)


; Problem A19

;; The number of ways to change TOTAL with DENOMS
;; At most MAX-COINS total coins can be used.
(define (count-change total denoms max-coins)
    (cond ((= total 0) 1) ((or (< total 0) (null? denoms) (= max-coins 0)) 0) ;; Base Cases
    (else (+ (count-change total (cdr denoms) max-coins)
    (count-change (- total (car denoms)) denoms (- max-coins 1)))))) ;; Recursive Call
(define us-coins '(50 25 10 5 1))
(count-change 20 us-coins 18)
; expect 8

; Problem B20

;; The number of ways to partition TOTAL, where
;; each partition must be at most MAX-VALUE
(define (count-partitions total max-value)
     (cond ((< total 0) 0)
        ((<= max-value 0) 0)
        ((= total 0) 1)
        (else (+ (count-partitions (- total max-value) max-value)
          (count-partitions total (- max-value 1))))
))
(count-partitions 5 3)
; expect 5
; Note: The 5 partitions are [[3 2] [3 1 1] [2 2 1] [2 1 1 1] [1 1 1 1 1]]

; Problem 21

;; A list of all ways to partition TOTAL, where each partition must
;; be at most MAX-VALUE and there are at most MAX-PIECES partitions.
(define (list-partitions total max-pieces max-value)
   (define (helper total max-pieces max-value partitions sofar)
    (cond ((< max-pieces 0) partitions)
          ((= total 0) (cons sofar partitions))
          ((<= max-value 0) partitions)
          (else (append (helper (- total max-value) (- max-pieces 1) max-value partitions (append sofar (list max-value))) (helper total max-pieces (- max-value 1) partitions sofar)))))
  (helper total max-pieces max-value '() '())
) 
(list-partitions 5 2 4)
; expect ((4 1) (3 2))

(list-partitions 7 3 5)
; expect ((5 2) (5 1 1) (4 3) (4 2 1) (3 3 1) (3 2 2))

; Draw the hax image using turtle graphics.
(define (hax n k)
  ; *** YOUR CODE HERE ***
  nil)


;;;;;;;;;;;;;;;;;;;;
;;; Extra credit ;;;
;;;;;;;;;;;;;;;;;;;;

; Tail call optimization test
(define (sum n total)
  (if (zero? n) total
    (sum (- n 1) (+ n total))))
(sum 1001 0)
; expect 501501
