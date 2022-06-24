<?php
class MyLinkedList {
    //  public $tail, $head;
    public function __construct($value)
    {
        $this->head = [
            "value" => $value,
            "next" => null
        ];
        $this->tail = $this->head; 
        print_r($this->head);
        $this->tail['next'] = "Hello";
        print_r($this->head);
    }

    public function append($val){
       
        $newNode = [
            "value" => $val,
            "next" => null
        ];

        $this->head['next'] = $newNode;
        // $this->head['next'] = $this->tail;
        $this->tail = $newNode;
        $this->customPrint($this->head);
        return $this;
        
    }

    public function delete(){
        //
    }

    public function customPrint($data){
        echo "<pre>";
        print_r($data);
        echo "</pre>";
    }
}


$myLinkedList = new MyLinkedList(10);

//append

$myLinkedList->append(5);

$myLinkedList->append(11);

$myLinkedList->append(15);

$myLinkedList->customPrint($myLinkedList);


