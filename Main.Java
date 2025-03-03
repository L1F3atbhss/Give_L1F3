package frc.robot;

import edu.wpi.first.wpilibj.TimedRobot;
import org.photonvision.PhotonCamera;
import org.photonvision.targeting.PhotonPipelineResult;
import org.photonvision.targeting.PhotonTrackedTarget;

import edu.wpi.first.cameraserver.CameraServer;
import edu.wpi.first.cscore.UsbCamera;
import edu.wpi.first.math.geometry.Transform3d;
import edu.wpi.first.wpilibj.motorcontrol.Spark;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;

public class Robot extends TimedRobot {

    private PhotonCamera camera; 
    private DifferentialDrive drivetrain;

    // Desired distance from the AprilTag (meters)
    private static final double DESIRED_DISTANCE = 1.0;
    // Proportional gain for driving forward/backward
    private static final double DRIVE_KP = 0.5;
    // Proportional gain for turning based on yaw error
    private static final double TURN_KP = 0.03;

    @Override
    public void robotInit() {
        // Initialize PhotonCamera with the name configured in your PhotonVision dashboard
        camera = new PhotonCamera("FHD_Camera");

        // Start camera streaming (useful for vision debugging)
        UsbCamera usbCamera = CameraServer.startAutomaticCapture();
        usbCamera.setResolution(352, 288);

        // Initialize drivetrain motors (assuming PWM ports 0 and 1)
        Spark leftMotor = new Spark(0);
        Spark rightMotor = new Spark(1);
        drivetrain = new DifferentialDrive(leftMotor, rightMotor);
    }

    @Override
    public void robotPeriodic() {
        // Get the latest vision processing result
        PhotonPipelineResult result = camera.getLatestResult();

        if (result.hasTargets()) {
            // Select the best target detected (e.g., the AprilTag)
            PhotonTrackedTarget target = result.getBestTarget();
            // Get the horizontal offset (yaw) to the target
            double yaw = target.getYaw();

            // Get the transform from the camera to the target if available
            Transform3d camToTarget = target.getBestCameraToTarget();
            if (camToTarget != null) {
                // Calculate the 3D distance from the camera to the target
                double distance = Math.sqrt(
                    Math.pow(camToTarget.getTranslation().getX(), 2) +
                    Math.pow(camToTarget.getTranslation().getY(), 2) +
                    Math.pow(camToTarget.getTranslation().getZ(), 2)
                );

                // Debug outputs
                System.out.println("Distance to Target: " + distance);
                System.out.println("Yaw to Target: " + yaw);

                // Compute commands:
                //   - Forward speed is proportional to the error between current and desired distance.
                //   - Turn command is proportional to the yaw (horizontal offset) to align with the target.
                double driveCommand = (distance - DESIRED_DISTANCE) * DRIVE_KP;
                double turnCommand = yaw * TURN_KP;

                // Send computed commands to the drivetrain
                drivetrain.arcadeDrive(driveCommand, turnCommand);
            }
        } else {
            // No target detected: stop the robot
            drivetrain.arcadeDrive(0, 0);
            System.out.println("No targets detected.");
        }
    }
}
