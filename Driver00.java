
import javax.swing.*;
import java.io.*;
import javax.imageio.ImageIO;
import java.awt.image.*;

public class Driver00 {
   
   public static void main(String[] args) throws IOException {
      
      
      JFrame frame = new JFrame("Tile");
      
      String path="dungeonTile.jpg";
      File file= new File(path);
      BufferedImage image = ImageIO.read(file);
      JLabel label = new JLabel(new ImageIcon(image));
      
      //frame.setLayout(null);
      //frame.pack();  
      frame.setSize(400,400);
      frame.setLocation(200,200);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.getContentPane().add(label);
      
      frame.setVisible(true);
   }
}