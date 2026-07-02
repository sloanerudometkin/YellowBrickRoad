package rocks.zipcode.dreamhouse;

import java.awt.*;

/**
 * A triangle that can be manipulated and that draws itself on a canvas.
 *
 * @author  Michael Kölling and David J. Barnes
 * @version 1.0  (15 July 2000)
 */

public class Triangle extends Shape
{
    private int height;
    private int width;

    /**
     * Create a new triangle at default position with default color.
     */
    public Triangle()
    {
        super(50, 15, "green");
        height = 30;
        width = 40;
    }

    /**
     * Change the size to the new size (in pixels). Size must be >= 0.
     */
    public void changeSize(int newHeight, int newWidth)
    {
        erase();
        height = newHeight;
        width = newWidth;
        draw();
    }

    /*
     * Draw the triangle with current specifications on screen.
     */
    protected void draw()
    {
        if(isVisible) {
            Canvas canvas = Canvas.getCanvas();
            int[] xpoints = { xPosition, xPosition + (width/2), xPosition - (width/2) };
            int[] ypoints = { yPosition, yPosition + height, yPosition + height };
            canvas.draw(this, color, new Polygon(xpoints, ypoints, 3));
            canvas.wait(10);
        }
    }
}
