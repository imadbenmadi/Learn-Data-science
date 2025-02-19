**short summary** of Matplotlib’s architecture:

### 🔹 **Three Main Layers:**
1. **Backend Layer:**  
   - Handles rendering (drawing on the screen).
   - Manages user inputs (mouse clicks, keyboard strokes).
   - Contains:
     - `FigureCanvas` (where the figure is drawn).
     - `Renderer` (knows how to draw elements).
     - `Event` (handles user interactions).

2. **Artist Layer:**  
   - Contains everything that is drawn (titles, labels, lines, points, etc.).
   - Two types of artists:
     - **Primitive** (basic elements like `Line2D`, `Rectangle`, `Text`).
     - **Composite** (complex structures like `Axis`, `Figure`).

3. **Scripting Layer (Pyplot):**  
   - **Simplified interface** for quick plotting.
   - Automatically creates a figure and canvas.
   - Best for everyday data visualization tasks.

### 🔹 **Anatomy of a Plot:**
- **Figure** → The overall container.
- **Axes** → The individual plots inside a figure.
- **Title, Labels, Legend, Grid, Annotations** → Extra elements for better readability.

👉 **For quick usage**, you only need the scripting layer (`matplotlib.pyplot`).  
For more control (like in web apps), you’d interact with the **backend and artist layers**.