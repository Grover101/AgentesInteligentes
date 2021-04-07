class Thing:
    """Representa cualquier objeto físico que pueda aparecer en un entorno.
    Subclase Thing para obtener las cosas que desea. Cada cosa puede tener un
    .__ name__ slot (usado solo para salida)."""

    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def is_alive(self):
        """Las cosas que están 'vivas' deberían volver a ser verdaderas."""
        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        """Muestra el estado interno del agente. Las subclases deben anular."""
        print("No sé cómo mostrar el estado.")

    def display(self, canvas, x, y, width, height):
        """Muestre una imagen de esta cosa en el lienzo."""
        # Do we need this?
        pass
