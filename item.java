public abstract class item extends inventory {

   public item(String name, String hoverText) {
      super(name,hoverText);
   }
   
   public abstract void use(); //causes effect of item
   
   public abstract void shatter(); //unique message, and possibly effects, each time.
   
   
}