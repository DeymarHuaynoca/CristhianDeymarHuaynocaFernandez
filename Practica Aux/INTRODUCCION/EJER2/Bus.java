package INTRODUCCION.EJER2;

class Bus {
    private int capacidadTotal;
    private int pasajerosActuales;
    private double costoPasaje = 1.50;

    public Bus(int capacidadTotal) {
        this.capacidadTotal = capacidadTotal;
        this.pasajerosActuales = 0;
    }

    public void subirPasajeros(int cantidad) {
        if (pasajerosActuales + cantidad <= capacidadTotal) {
            pasajerosActuales += cantidad;
            System.out.println(cantidad + " pasajeros subieron al bus.");
        } else {
            int disponibles = capacidadTotal - pasajerosActuales;
            System.out.println("Solo pueden subir " + disponibles + " pasajeros, el resto no entra.");
            pasajerosActuales = capacidadTotal;
        }
    }

    public double cobrarPasaje() {
        double total = pasajerosActuales * costoPasaje;
        System.out.println("Se recaudo Bs. " + total + " en pasajes.");
        return total;
    }

    public void mostrarAsientosDisponibles() {
        int disponibles = capacidadTotal - pasajerosActuales;
        System.out.println("Asientos disponibles: " + disponibles);
    }
}
