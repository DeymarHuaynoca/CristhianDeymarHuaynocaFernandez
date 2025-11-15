class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;

    public Empleado(String nombre, String cargo, double sueldo) {
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        return nombre + " - " + cargo + " - $" + sueldo;
    }
}

class Departamento {
    private String nombre;
    private String area;
    private java.util.List<Empleado> empleados;

    public Departamento(String nombre, String area) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = new java.util.ArrayList<>();
    }

    public Departamento(String nombre, String area, java.util.List<Empleado> empleados) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = empleados;
    }

    public java.util.List<Empleado> getEmpleados() {
        return empleados;
    }

    public void mostrarEmpleados() {
        System.out.println("\nDepartamento: " + nombre + " (" + area + ")");
        if (empleados.isEmpty()) {
            System.out.println("  No hay empleados.");
            return;
        }
        for (Empleado emp : empleados) {
            System.out.println("  " + emp);
        }
    }

    public void cambioSalario(double nuevoSueldo) {
        for (Empleado emp : empleados) {
            emp.setSueldo(nuevoSueldo);
        }
    }
}

public class Main {
    public static boolean verificarEmpleado(Departamento depOrigen, Departamento depDestino) {
        for (Empleado emp : depOrigen.getEmpleados()) {
            if (depDestino.getEmpleados().contains(emp)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        java.util.List<Empleado> empleadosDep1 = new java.util.ArrayList<>();
        empleadosDep1.add(new Empleado("Ana", "Analista", 4000));
        empleadosDep1.add(new Empleado("Luis", "Programador", 3500));
        empleadosDep1.add(new Empleado("Maria", "Diseñadora", 3800));
        empleadosDep1.add(new Empleado("Carlos", "Tester", 3200));
        empleadosDep1.add(new Empleado("Jose", "DevOps", 4500));

        Departamento departamento1 = new Departamento("TI", "Tecnologia", empleadosDep1);
        Departamento departamento2 = new Departamento("RRHH", "Recursos Humanos");

        System.out.println("=== Empleados Departamento 1 ===");
        departamento1.mostrarEmpleados();

        System.out.println("=== Empleados Departamento 2 ===");
        departamento2.mostrarEmpleados();

        System.out.println("\nAplicando aumento de sueldo a TODOS en departamento 1...");
        departamento1.cambioSalario(5000);

        System.out.println("\n=== Departamento 1 (sueldos actualizados) ===");
        departamento1.mostrarEmpleados();

        System.out.println("\n¿Algún empleado de dep1 pertenece tambien a dep2?: " +
                verificarEmpleado(departamento1, departamento2));

        System.out.println("\nMoviendo empleados del departamento 1 al departamento 2...");

        departamento2.getEmpleados().addAll(departamento1.getEmpleados());
        departamento1.getEmpleados().clear();

        System.out.println("\n=== Departamento 1 (ahora vacio) ===");
        departamento1.mostrarEmpleados();

        System.out.println("=== Departamento 2 (ahora con empleados) ===");
        departamento2.mostrarEmpleados();
    }
}
