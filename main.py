import plotly.graph_objects as go
import numpy as np

# Utility functions
def create_cuboid(x, y, z, dx, dy, dz, color):
    x0, x1 = x - dx/2, x + dx/2
    y0, y1 = y - dy/2, y + dy/2
    z0, z1 = z - dz/2, z + dz/2
    vertices = [
        [x0, y0, z0], [x1, y0, z0], [x1, y1, z0], [x0, y1, z0],
        [x0, y0, z1], [x1, y0, z1], [x1, y1, z1], [x0, y1, z1]
    ]
    x_vals, y_vals, z_vals = zip(*vertices)
    faces = [
        [0,1,2], [0,2,3], [4,5,6], [4,6,7],
        [0,1,5], [0,5,4], [2,3,7], [2,7,6],
        [1,2,6], [1,6,5], [3,0,4], [3,4,7]
    ]
    i, j, k = zip(*faces)
    return go.Mesh3d(x=x_vals, y=y_vals, z=z_vals, i=i, j=j, k=k, color=color, opacity=1.0)

def create_cylinder(x, y, z, height, radius, axis='y', segments=20, color='gray'):
    theta = np.linspace(0, 2*np.pi, segments)
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)

    if axis == 'y':
        xs = np.concatenate([x + circle_x, x + circle_x])
        ys = np.concatenate([y + np.full(segments, 0), y + np.full(segments, height)])
        zs = np.concatenate([z + circle_y, z + circle_y])
    else:
        raise NotImplementedError("Only y-axis cylinders implemented")

    faces = []
    for i in range(segments-1):
        faces.append([i, i+1, i+segments+1])
        faces.append([i, i+segments+1, i+segments])
    faces.append([segments-1, 0, segments])
    faces.append([segments-1, segments, segments*2-1])
    i, j, k = zip(*faces)
    return go.Mesh3d(x=xs, y=ys, z=zs, i=i, j=j, k=k, color=color, opacity=1.0)

def create_sphere(x, y, z, r, color='black'):
    phi = np.linspace(0, np.pi, 20)
    theta = np.linspace(0, 2 * np.pi, 20)
    phi, theta = np.meshgrid(phi, theta)
    xs = x + r * np.sin(phi) * np.cos(theta)
    ys = y + r * np.sin(phi) * np.sin(theta)
    zs = z + r * np.cos(phi)
    return go.Surface(x=xs, y=ys, z=zs, colorscale=[[0, color], [1, color]], showscale=False)

# Scene assembly
def build_robot():
    parts = []
    torso_thickness = 0.5  # Sebelumnya 1.0 atau 1.5

    # Torso (lebih ramping dari samping)
    parts.append(create_cuboid(0, 4, 0, 2, 4, torso_thickness, 'lightgray'))
    parts.append(create_cuboid(0, 4.3, torso_thickness/2, 1.7, 1.2, 0.04, 'deepskyblue'))

    # Head (diperkecil ketebalannya juga)
    parts.append(create_cuboid(0, 7.2, 0, 1.5, 1.5, 0.9, 'lightgray'))
    parts.append(create_cylinder(0, 6, 0, 0.4, 0.2, axis='y', color='gray'))
    parts.append(create_cylinder(0, 8.1, 0, 0.6, 0.08, axis='y', color='deepskyblue'))

    # Eyes (disesuaikan ke depan wajah)
    parts.append(create_sphere(-0.3, 7.4, 0.45, 0.15, 'black'))
    parts.append(create_sphere( 0.3, 7.4, 0.45, 0.15, 'black'))

    # Arms (lebih tipis juga dari samping)
    parts.append(create_cuboid(-1.2, 4.5, 0, 0.4, 2.5, 0.3, 'silver'))  # Left arm
    parts.append(create_cuboid( 1.2, 4.5, 0, 0.4, 2.5, 0.3, 'silver'))  # Right arm

    # Legs (lebih ramping dari depan dan samping)
    parts.append(create_cuboid(-0.5, 1.2, 0, 0.5, 2.2, 0.4, 'dimgray'))  # Left leg
    parts.append(create_cuboid( 0.5, 1.2, 0, 0.5, 2.2, 0.4, 'dimgray'))  # Right leg

    return parts

if __name__ == '__main__':
    parts = build_robot()
    fig = go.Figure(data=parts)
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='data',
            bgcolor="rgb(5,5,10)"
        ),
        margin=dict(r=0, l=0, b=0, t=0)
    )
    fig.show()
