import mujoco
import mujoco.viewer
import numpy as np

mjcf = """
<mujoco>
    <compiler coordinate="local"/>
    <option gravity="0 0 0" timestep="0.0005" integrator="RK4"/>

    <default>
        <joint damping="2" armature="0.01"/>
        <geom density="1000"/>
    </default>

    <worldbody>

        <!-- Crank -->
        <body name="crank" pos="0 0 0">
            <joint name="theta" type="hinge" axis="0 0 1"/>
            <geom type="capsule" fromto="0 0 0 0.5 0 0" size="0.04"/>

            <!-- Connecting rod -->
            <body name="rod" pos="0.5 0 0">
                <joint name="phi" type="hinge" axis="0 0 1"/>
                <geom type="capsule" fromto="0 0 0 1.0 0 0" size="0.035"/>

                <site name="rod_tip" pos="1.0 0 0" size="0.02"/>
            </body>
        </body>

        <!-- Slider (solo eje X) -->
        <body name="slider" pos="1.5 0 0">
            <joint name="x" type="slide" axis="1 0 0"/>
            <geom type="box" size="0.15 0.1 0.1"/>
            <site name="slider_pin" pos="0 0 0" size="0.02"/>
        </body>

    </worldbody>

    <!-- Cierre de loop -->
    <equality>
        <connect site1="rod_tip" site2="slider_pin"/>
    </equality>

    <actuator>
        <!-- Torque reducido -->
        <motor joint="theta" ctrlrange="-5 5" gear="1"/>
    </actuator>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(mjcf)
data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():

        # Torque pequeño y control suave
        data.ctrl[0] = 1.5

        mujoco.mj_step(model, data)
        viewer.sync()