class LinkedList {
    private Node head = null;
    private int len = 0;

    public LinkedList() {
    }

    public int get(int index) {
        if (index >= len){
            return -1;
        }
        Node n = head;
        for(int i = 1; i < index + 1; i++){
            n = n.getNext();
        }
        return n.getVal();
    }

    public void insertHead(int val) {
        this.head = new Node(val, this.head);
        len++;
    }

    public void insertTail(int val) {
        if(head == null){
            insertHead(val);
        }
        else {
            Node currNode = head;
            Node insNode = new Node(val, null);
            while(currNode.getNext() != null){
                currNode = currNode.getNext();
            }
            currNode.setNext(insNode);
            len++;
        }

    }

    public boolean remove(int index) {
        if(index >= len){
            return false;
        }
        if(index == 0){
            head = head.getNext();
        }
        else {
            Node oneBefore = head;
            for(int i = 0; i < index-1; i++){
                oneBefore = oneBefore.getNext();
            }
            Node toRet = oneBefore.getNext();
            oneBefore.setNext(toRet.getNext());
        }
        len--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> arl = new ArrayList<>();
        Node n = head;
        for(int i = 0; i < len; i++){
            arl.add(n.getVal());
            n = n.getNext();
        }
        return arl;
    }
}

class Node {
    private int val;
    private Node next;

    public Node(int val, Node next){
        this.val = val;
        this.next = next;
    }

    public int getVal(){
        return val;
    }

    public void setVal(int n){
        val = n;
    }

    public Node getNext(){
        return next;
    }

    public void setNext(Node n){
        next = n;
    }
}