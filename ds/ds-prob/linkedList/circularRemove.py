class Node(object) :
	def __init__(self, data) :
		self.data = data
		self.next = None

head    = Node(1)
second  = Node(2)
third   = Node(3)
fourth  = Node(4)
fifth   = Node(5)
sixth   = Node(6)
seventh = Node(7)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh
seventh.next = third


def findCircular() :
    current = head
    current2 = head

    circuler = None
    while current2 is not None:
        current = current.next
        current2 = current2.next.next

        if current == current2 :
            circuler = current
            print("circuler ll found ", circuler.data)
            return circuler

def way1() :
    circuler = findCircular()

    from_head = head
    from_circular = circuler
    exact_circular = None

    while from_circular is not None :
        exact_circular = from_circular
        from_circular = from_circular.next
        from_head = from_head.next

        if from_head == circuler :
            from_head = head

        if from_head == from_circular :
            print("exact_circular point to break", exact_circular.data, from_circular.data)
            exact_circular.next = None
            break

    after_r = head
    while after_r is not None :
        print(after_r.data)
        after_r = after_r.next

# way1()

def way2() :
    circuler = findCircular()

    initial = circuler
    lengthOfCircularLoop = 0

    while True :
        initial = initial.next
        lengthOfCircularLoop += 1

        if initial == circuler:
            break

    print("lengthOfCircularLoop", lengthOfCircularLoop)

    main = head
    mainLOCL = head

    for i in range(lengthOfCircularLoop) :
        mainLOCL = mainLOCL.next

    mainLOCLPrev = None
    while mainLOCL is not main :
        mainLOCLPrev = mainLOCL
        main = main.next
        mainLOCL = mainLOCL.next

    print(mainLOCLPrev.data)
    mainLOCLPrev.next = None

    after_r = head
    while after_r is not None :
        print(after_r.data)
        after_r = after_r.next



way2()



