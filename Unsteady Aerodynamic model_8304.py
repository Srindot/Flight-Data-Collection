
import pterasoftware as ps
import numpy as np
import matplotlib.pyplot as plt
from SelfFunctions import extract_forces, extract_second_cycle, save_flight_data_to_csv

# Function call for the unsteady aerodynamic model with the NACA 8304 airfoil
def simulation(va= 5, aoa = 5, ff = 0.2):
    example_airplane=ps.geometry.Airplane(
        name="naca8304",
        x_ref=0.11,
        y_ref=0.0,
        z_ref=0.0,
        s_ref=None,
        b_ref=None,
        c_ref=None,
        wings=[
            ps.geometry.Wing(
                name="Main Wing",
                x_le=0.0,
                y_le=0.0,
                z_le=0.0,
                symmetric=True,
                num_chordwise_panels=6,
                chordwise_spacing="cosine",
                wing_cross_sections=[
                    ps.geometry.WingCrossSection(
                        x_le=0.0,
                        y_le=0.0,
                        z_le=0.0,
                        twist=0.0,
                        control_surface_type="symmetric",
                        control_surface_hinge_point=0.0,
                        control_surface_deflection=0.0,
                        num_spanwise_panels=8,
                        spanwise_spacing="cosine",
                        chord=0.3,
                        airfoil=ps.geometry.Airfoil(
                            name="naca8304",
                            coordinates=None,
                            repanel=True,
                            n_points_per_side=400,
                        ),
                    ),
                    ps.geometry.WingCrossSection(
                        x_le=0.0,
                        y_le=0.7,
                        z_le=0.0,
                        chord=0.2,
                        twist=0.0,
                        airfoil=ps.geometry.Airfoil(
                            name="naca8304",
                        ),
                    ),
                ],
            ),
            ps.geometry.Wing(
                name="V-Tail",
                x_le=0.45,
                y_le=0.0,
                z_le=0.0,
                num_chordwise_panels=6,
                chordwise_spacing="cosine",
                symmetric=True,
                wing_cross_sections=[
                    ps.geometry.WingCrossSection(
                        chord=0.2,
                        control_surface_type="symmetric",
                        control_surface_hinge_point=0.1,
                        control_surface_deflection=0.0,
                        airfoil=ps.geometry.Airfoil(
                            name="naca0004",
                        ),
                        twist=0.0,
                    ),
                    ps.geometry.WingCrossSection(
                        x_le=0.19,
                        y_le=0.2,
                        z_le=0.003,
                        chord=0.01,
                        control_surface_type="symmetric",
                        control_surface_hinge_point=0.1,
                        control_surface_deflection=0.0,
                        twist=0.0,
                        airfoil=ps.geometry.Airfoil(
                            name="naca0004",
                        ),
                    ),
                ],
            ),
        ],
    )
    main_wing_root_wing_cross_section_movement=ps.movement.WingCrossSectionMovement(
        base_wing_cross_section=example_airplane.wings[0].wing_cross_sections[0],
    )
    main_wing_tip_wing_cross_section_movement=ps.movement.WingCrossSectionMovement(
        base_wing_cross_section=example_airplane.wings[0].wing_cross_sections[1],
        sweeping_amplitude=30.0,
        #____________________________________________________________________
        sweeping_period=ff,
        #____________________________________________________________________
        sweeping_spacing="sine",
        pitching_amplitude=0.0,
        pitching_period=0.0,
        pitching_spacing="sine",
        heaving_amplitude=0.0,
        heaving_period=0.0,
        heaving_spacing="sine",
    )
    v_tail_root_wing_cross_section_movement=ps.movement.WingCrossSectionMovement(
        base_wing_cross_section=example_airplane.wings[1].wing_cross_sections[0],
    )
    v_tail_tip_wing_cross_section_movement=ps.movement.WingCrossSectionMovement(
        base_wing_cross_section=example_airplane.wings[1].wing_cross_sections[1],
    )
    main_wing_movement=ps.movement.WingMovement(
        base_wing=example_airplane.wings[0],
        wing_cross_sections_movements=[
            main_wing_root_wing_cross_section_movement,
            main_wing_tip_wing_cross_section_movement,
        ],
    )
    del main_wing_root_wing_cross_section_movement
    del main_wing_tip_wing_cross_section_movement
    v_tail_movement=ps.movement.WingMovement(
        base_wing=example_airplane.wings[1],
        wing_cross_sections_movements=[
            v_tail_root_wing_cross_section_movement,
            v_tail_tip_wing_cross_section_movement,
        ],
    )
    del v_tail_root_wing_cross_section_movement
    del v_tail_tip_wing_cross_section_movement
    airplane_movement=ps.movement.AirplaneMovement(
        base_airplane=example_airplane,
        wing_movements=[main_wing_movement,v_tail_movement],
    )
    del main_wing_movement
    del v_tail_movement
    example_operating_point=ps.operating_point.OperatingPoint(
        #____________________________________________________________________
        density=1.225,
        beta=0.0,
        velocity=va,
        alpha=aoa,
        nu=15.06e-6,
        external_thrust=0.0,
        #____________________________________________________________________
    )
    operating_point_movement=ps.movement.OperatingPointMovement(
        base_operating_point=example_operating_point,
        velocity_amplitude=0.0,
        velocity_period=0.0,
        velocity_spacing="sine",
    )
    movement=ps.movement.Movement(
        airplane_movements=[airplane_movement],
        operating_point_movement=operating_point_movement,
        num_steps=None,
        delta_time=None,
    )
    del airplane_movement
    del operating_point_movement
    example_problem=ps.problems.UnsteadyProblem(
        movement=movement,
    )
    example_solver=ps.unsteady_ring_vortex_lattice_method.UnsteadyRingVortexLatticeMethodSolver(
        unsteady_problem=example_problem,
    )
    del example_problem
    example_solver.run(
        logging_level="Warning",
        prescribed_wake=True,
    )

    # ps.output.print_unsteady_results(unsteady_solver=example_solver)
    # ps.output.plot_results_versus_time(
    #     unsteady_solver=example_solver,
    #     show=False,
    #     save=True,
    # )

#     ps.output.animate(
#     unsteady_solver=example_solver,
#     scalar_type="lift",
#     show_wake_vortices=True,
#     # Tell the animate function to not save the animation as file. This way,
#     # the animation will still be displayed but not saved. This value defaults to
#     # false.
#     save=True,
# )

    lift, induced_drag, side_force, pitching_moment = extract_forces(example_solver)  

    return lift, induced_drag, side_force, pitching_moment


#Giving values for the input for the function call
# Flapping_Fequency = range(0.6, 1.2, 0.1)
# Angle_of_Attack = range(-30, 30, 5)
# Air_Speed = range(1, 6, 0.5)

# va= 3
# aoa = -0
# ff = 0.2

# # Function call
# lift, induced_drag, side_force, pitching_moment = simulation(va, aoa, ff)

# lift = lift.flatten()
# induced_drag = induced_drag.flatten()
# side_force = side_force.flatten()
# pitching_moment = pitching_moment.flatten()


# print("Before Second Cycle Extraction :  ", lift.shape, induced_drag.shape, pitching_moment.shape)
# print("Before Second Cycle Extraction value:  ", lift, induced_drag, pitching_moment)

# lift, induced_drag, pitching_moment = extract_second_cycle(lift, induced_drag, pitching_moment)

# print("After Second Cycle Extraction :  ",lift.shape, induced_drag.shape, pitching_moment.shape)
# print("After Second Cycle Extraction value:  ", lift, induced_drag, pitching_moment)


# save_flight_data_to_csv(ff, va, aoa, lift, pitching_moment, induced_drag, "flapping.csv")



n = 0
for i in FlappingPeriod:
    for j in Air_Speed:
        for k in Angle_of_Attack:
            #D Increament Parameter to count the number of CSV Files
            # Call simulation function with Airspeed (k), AoA (j), and Flapping Frequency (i)
            lift, induced_drag, pitching_moment = simulation(j, k, i)

            # Flatten the shit out of them
            lift = lift.flatten()
            induced_drag = induced_drag.flatten()
            pitching_moment = pitching_moment.flatten()
            print("Before Second Cycle Extraction :  ", lift.shape, induced_drag.shape, pitching_moment.shape)
            print("Before Second Cycle Extraction value:  ", lift, induced_drag, pitching_moment)
            
            # Extract the second cycle from the data
            lift, induced_drag, pitching_moment = extract_second_cycle(lift, induced_drag, pitching_moment, i)
            print("After Second Cycle Extraction :  ",lift.shape, induced_drag.shape, pitching_moment.shape)
            print("After Second Cycle Extraction value:  ", lift, induced_drag, pitching_moment)
            # Save data to CSV with a unique filename for each combination
            file_name = f"flapping{n}.csv"
            n += 1
            save_flight_data_to_csv(i, j, k, lift, pitching_moment, induced_drag, file_name)




