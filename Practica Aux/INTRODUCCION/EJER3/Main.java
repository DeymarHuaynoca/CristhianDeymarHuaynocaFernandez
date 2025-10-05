package INTRODUCCION.EJER3;

public class Main {
    public static void main(String[] args) {

        Producto p1 = new Producto("Galletas", 3.5, 10);

        p1.vender(4);
        p1.vender(8);

        p1.reabastecer(20);
        p1.vender(5);
    }
}
