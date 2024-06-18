During my junior year of high school, I spent one of my class slots independently doing graphics programming projects.

I used the assignment specifications from MIT's [Fall 2012 Computer Graphics](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/pages/assignments/) course, timeless exercises covering a range of basic graphics programming concepts.

The graphics stack the assignments prescribed (OpenGL 2, C++03) is heavily out of date. I used their assets so that I wouldn't have to
create new ones, but I wrote the projects from scratch with Rust and wgpu.
Annoyingly, this meant I had to write several parsers for their bespoke formats.

All of my implementations adhere to the spirit of the assignments, although a few don't exactly fulfill the specifications.

The code is [available on GitHub]("https://github.com/allie-m/projectstudio"), along
with instructions for how to run it.

## Obj Parser and Renderer

| | |
|:--|:--|
| ![](../assets/projects/projectstudio/garg.png){ width=260 } | Warmup exercise! This program parses obj files and renders their models interactively.<br><br>See the "garg" pictured left. |

## Swept Surfaces Renderer

| | |
|:--|:--|
| ![](../assets/projects/projectstudio/flircle.png){ width=260 } | This program triangulates and interactively renders meshes based on a swept surface representation.<br><br>These swept surfaces are defined mostly from bezier curves and B-splines.<br><br>See the "flircle" pictured left.|

## Skeletal Modeling

| | |
|:--|:--|
| ![](../assets/projects/projectstudio/skeletalmodel.png){ width=260 } | This program renders and animates skeletal models with bone hierarchies.<br><br>The shader is generic and can handle any transformation of any bone hierarchy. However, the program is hardcoded to swing the legs of the input model, since all the sample models have the same bone structure.|

## Particle-Based Cloth Simulation

This program models the physics of a cloth --- specifically, a flag flapping in the breeze --- with a particle based simulation.

Each particle is acted on by forces (gravity, wind, and springs binding the cloth together), and an
[rk4 numerical integrator](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods),
implemented in compute shaders, turns the forces into velocities that allow the cloth's motion to be simulated in real time.

<img src="../assets/projects/projectstudio/flagrainbow.png" width="290" height="290">
<img src="../assets/projects/projectstudio/flagtrans.png" width="290" height="290">

## Basic Raytracer

This program renders basic scenes with a custom raytracer implemented in a compute shader.
It is direct illumination only, though it does support reflections.
I considered trying to implement proper global illumination, but realized I would have to rearchitect the program.
I decided against it, as it is not in the course specification.

<img src="../assets/projects/projectstudio/spheres.png" width="290" height="290">
<img src="../assets/projects/projectstudio/bunny.png" width="290" height="290">

## Terrain Renderer

This was not an assignment specification, but something I did because I had extra time.
I found ultra-high resolution heightmap data for Alameda County and used
<a href="https://github.com/heremaps/tin-terrain">tin-terrain</a> to convert it into
chunked meshes at varying levels of detail, which my program then rendered.

You can't actually see all of Alameda County at once, only the slice of it I processed.
Still, the detail is remarkable. Too bad they didn't have data underneath the waters of Lake Chabot (featured below),
it would have been nice to do some water rendering.

<img src="../assets/projects/projectstudio/alamedacounty.png" width="100%">