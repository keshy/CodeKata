// write a method to reverse the word order in a given sentence
// ie, input: reverse the words
// output: words the rever

public String reverseWordsInSentence(String sentence) {

   // check if sentence exists
   if (sentence == null) {
       return null;
   }
   // assuming no punctuation
   List<String> words = sentence.split(" ")
   // if there is only one word - the reverse is the word itself
   if (words.length == 1) {
       return sentence;
   }

   // use string builder as String is immutable
   StringBuilder builder = new StringBuilder();
   for (i = words.length - 1; i>= 0; i--) {
       builder.append(words[i]);
       if (i != 0) {
           builder.append(" ");
       }

   }


   return builder.toString();
}


public class Node {
    private int value;
    Node prev;
    Node next;
}

// assume this is NOT a circular list
public class DoublyLinkedList {
    private Node head;


    public void insertNewNodeAtPositionN (Node newNode, int n) {
        int index = 1
        // 0 is invalid
        if (n == 0) {
            return;
        }
        // n == 1
        if (n == 1) {
            // insert before head
            newNode.next = head;
            head.prev = newNode;
            newNode.prev = null;
            head = newNode;
        }
        // n > 1

        Node temp = head;
        Node tempNext = head.next;

        // node1 -> node2 ->node3
        // insert node4 in 2

        while(index < n) {
            temp = temp.next;
            tempNext = temp.next;
            index += 1
        }

        temp.next = newNode;
        newNode.prev = temp;
        tempNext.prev = newNode;

        return;

    }
}