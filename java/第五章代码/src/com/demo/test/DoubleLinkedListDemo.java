package com.demo.test;

import com.demo.doublylist.DoubleLinkedList;
import com.demo.doublylist.DoubleLinkedList.Node;

public class DoubleLinkedListDemo {
    public static void main(String[] args) {
        DoubleLinkedList list = new DoubleLinkedList(10);
        Node [] nodes = new Node[10];

        for (int i = 0; i < nodes.length; i++){
            Node node = new Node(i, i);
            nodes[i] = node;
        }

        list.append(nodes[0]);
        list.print();


        list.append(nodes[1]);
        list.print();

        list.pop();
        list.print();

        list.append(nodes[2]);
        list.print();

        list.appendFront(nodes[3]);
        list.print();

        list.append(nodes[4]);
        list.print();

        list.remove(nodes[2]);
        list.print();

        list.remove(null);
        list.print();
    }

}
