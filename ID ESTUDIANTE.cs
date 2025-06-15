using System;

namespace RegistroEstudiantes
{
    // Clase principal que representa a un estudiante
    public class Estudiante
    {
        // Propiedades
        public int Id { get; set; }
        public string Nombres { get; set; }
        public string Apellidos { get; set; }
        public string Direccion { get; set; }
        public string[] Telefonos { get; set; } // Array para 3 teléfonos

        // Constructor
        public Estudiante(int id, string nombres, string apellidos, string direccion, string[] telefonos)
        {
            // Validar que el array tenga 3 teléfonos
            if (telefonos.Length != 3)
                throw new ArgumentException("Debe ingresar exactamente 3 teléfonos.");

            Id = id;
            Nombres = nombres;
            Apellidos = apellidos;
            Direccion = direccion;
            Telefonos = telefonos; // Asignar el array completo
        }

        // Método para mostrar datos del estudiante
        public void MostrarDatos()
        {
            Console.WriteLine($"ID: {Id}");
            Console.WriteLine($"Nombre: {Nombres} {Apellidos}");
            Console.WriteLine($"Dirección: {Direccion}");
            Console.WriteLine("Teléfonos:");
            for (int i = 0; i < Telefonos.Length; i++)
            {
                Console.WriteLine($"  {i + 1}. {Telefonos[i]}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Ejemplo de uso
            string[] telefonos = { "0991234567", "022987654", "0987654321" };
            
            // Crear instancia de Estudiante
            Estudiante estudiante1 = new Estudiante(
                id: 1,
                nombres: "María",
                apellidos: "López",
                direccion: "Av. Principal 123",
                telefonos: telefonos // Pasar el array
            );

            // Mostrar datos
            estudiante1.MostrarDatos();
        }
    }
}