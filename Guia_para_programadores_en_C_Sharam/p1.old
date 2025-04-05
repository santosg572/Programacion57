#include <iostream>
using namespace std;

const int maxCard = 16;
enum Bool { False, True };
enum ErrCode { noErr, overflow };

class Set {
   int elems[maxCard];
   int card;
public:
   void EmptySet () { card = 0; }
   Bool Member (int );
   ErrCode AddElem (int);
   void RmvElem (int);
   void Copy (Set *);
   Bool Equal (Set *);
   void Print ();
   void Intersect (Set *, Set *);
   ErrCode Union (Set *, Set *);
};

Bool Set::Member (int elem)
{
   for (int i=0; i < card; ++i)
      if (elems[i] == elem)
         return True;
   return False;
}


ErrCode Set::AddElem (int elem)
{
   for (int i=0; i < card; ++i)
      if (elems[i] == elem) return noErr;
   if (card < maxCard) {
      elems[card++] = elem; return noErr;
   } else
      return overflow;
}


void Set::RmvElem (int elem)
{
   for (int i = 0; i < card; ++i)
      if (elems[i] == elem) {
         for (; i < card -1 ; ++i)
            elems[i] = elems[i+1];
         --card;
      }
}


void Set::Copy (Set *set)
{
   for (int i=0; i < card; ++i)
      set -> elems[i] = card;
   set -> card = card;
}


Bool Set::Equal (Set *set)
{
   if (card != set -> card) return False;
   for (int i=0; i < card; ++i)
      if (!set -> Member(elems[i]))
         return False;
   return True;
}


void Set::Print ()
{
   cout << "{";
   for (int i=0; i < card-1; ++i)
      cout << elems[i] << ",";
   if (card > 0)
      cout << elems[card-1];
   cout << "}";
}


int main()
{
   Set s1, s2, s3;
   s1.EmptySet(); 
   s2.EmptySet(); 
   s3.EmptySet();

   s1.AddElem(10); 
   s1.AddElem(20);
   s1.AddElem(30);
   s1.AddElem(40);
   s2.AddElem(30); 
   s2.AddElem(50);
   s2.AddElem(10);
   s1.AddElem(60);
   
   cout << "s1 = ";	
   s1.Print();
   cout << "s2 = ";     
   s2.Print();

   s2.RmvElem(50);

   cout << "s2 - {50} = ";	
   s2.Print();

   if (s1.Member(20))
      cout << "20 is in s1\n";
   s1.Intersect(&s2, &s3);
   cout << "s1 intsec s2 = ";	
   s3.Print();
   s1.Union(&s2, &s3);
   cout << "s1 union s2 =";	
   s3.Print();
   if (!s1.Equal(&s2))
      cout << "s1 /= s2";
}

