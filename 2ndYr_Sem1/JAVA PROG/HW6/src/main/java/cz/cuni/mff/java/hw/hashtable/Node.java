package cz.cuni.mff.java.hw.hashtable;

/**
 * A simple node for a linked list.
 */
public class Node {
    Pair value;
    Node next;

    /**
     * Creates a new node.
     * @param value The value of the node.
     */
    Node(Pair value) {
        this.value = value;
        this.next = null;
    }
}