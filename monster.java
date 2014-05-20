public abstract class monster extends mob {
   //need to have the stats for dmg and armor.
   public monster(int x,int y,int direction, int health, int movespeed) {
      super(x,y,direction,health,movespeed);
   }
   public abstract void attack(hero victim);
   
}