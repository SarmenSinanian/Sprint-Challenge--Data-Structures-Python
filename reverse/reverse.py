class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    # edge case; if no head, return 'false'
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # Edge cases(empty list/solitary nodes)
    if self.head == None or self.head.get_next() == None:
      return
    else:
      # Set temp var old_head as current head
      old_head = self.head
      # Set temp var mid as the next item from current head
      mid = old_head.get_next()
      # Delete/set-to-None the reference to the old_head's original next node
      old_head.set_next(None)
      # While loop for when there is a mid and a next point
      while mid and mid.get_next():
        # Set temp var new_head as the next item from mid/old_head.get_next
        new_head = mid.get_next()
        # Change pointer from the next item to the previous item (from mid.next_node to old_head)
        mid.set_next(old_head)
        # Change old_head to mid as part of circular logic
        old_head = mid
        # Change mid to new_head as part of circular logic
        mid = new_head
      # Final reversal
      mid.set_next(old_head)
      # Finally setting tail as head
      self.head = mid
