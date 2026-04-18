class DynamicArray {
private:
    int * arr;
    int len;
    int cap;
public:
    DynamicArray(int capacity) {
        arr = new int[capacity];
        len = 0;
        cap = capacity;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (getSize() >= getCapacity()) {
            resize();
        }
        arr[len] = n;
        len++;
    }

    int popback() {
        if(len > 0){
            len--;
        };
        return arr[len];
    }

    void resize() {
        cap *= 2;
        int *temp = new int[cap];
        for(int i = 0; i < len; i++){
            temp[i] = arr[i];
        }
        delete[] arr;
        arr = temp;
    }

    int getSize() {
        return len;
    }

    int getCapacity() {
        return cap;
    }
};
