public class mob extends entity {

   public mob() {
   
      super(1,1,1);
   
   }
   
   public mob(int x,int y,int direction, int health, int movespeed) {
   
   }
   
   public void move() {
   
   }

   public void die() {
   
   }
   
   public boolean isAlive() {
      boolean status = true;
      return status;
   }
   
   public int getHealth() {
      int health=1;
      return health;
   }
   
  
}