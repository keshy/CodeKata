
Iterator implementation that iterates over a List<List<Integer>>


class IteratorImpl implements Iterator {

   List<List<T>> listCollection;
   Integer numLists;
   Integer currentList = 0;
   Iterator currrentIterator;

   public IteratorImpl(List<List<T>> lists) {
       this.listCollection = lists;
       this.numLists = lists.size();
   }


   public Iterator getIterator(){
       if (this.numLists < 1) {
           return null;
       }

       this.currentIterator = listCollection.get(0).iterator()
       return this.currentIterator;
   }

   @Override
   public Boolean hasNext() {

       if (!this.currentIterator.hasNext()) {
           if (this.currentList < this.numLists - 1) {
               this.currentIterator = listCollection.get(this.currentList++).iterator();
               return true;
           } else {
               return false;
           }
       } else {
           return this.currentIterator.hasNext();
       }

   }


   public T next() {
       if (this.hasNext()) {
           return this.currentIterator.next();
       } else {
           // End of List reached Exception
           return null;
       }

   }


   public T remove() {


       int curListSize = listCollection.get(this.currentList).size();
       if (curListSize == 0) {
          // move over to the next list

       }

       if (curListSize == 1) {
          // remove element and move to next list
       } else [
           // handle in a similar way as next()
       }

        if (this.hasNext()) {
           return this.currentIterator.remove();
       } else {
           // End of List reached Exception
           return null;
       }

   }
}


}

list<[1,2,3],[4,5,6],[7,8,9]>


////

Iterator it = getIterator(...);

while (it.hasNext()) {

  log(it.next());

}


while(true) {
  Integer foo =it.next();
  if (foo == null) {
    break;
  }
}



static Iterator getIterator(List<List<Integer>> lists)