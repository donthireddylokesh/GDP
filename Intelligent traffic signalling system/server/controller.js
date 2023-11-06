import VehicleModel from './model.js';
import express from "express";
const router = express.Router();

// import mongoose from "mongoose";
export const getPosts = async (req, res) => {
    try {
        const postMessage = await VehicleModel.find();
        res.status(200).json(postMessage);
    } catch (error) {
        res.status(404).json({ message: error.message });
    }
}

export const createLog = async (req,res) => {
        console.log(req.body);
        const log = new VehicleModel({
            vehicle_number: req.body.vehicle_number,
            time: req.body.time || new Date(),
            location: req.body.location,
        });
        try {
            const savedLog = await log.save();
            res.json(savedLog);
        } catch (err) {
            res.json({ message: err });
        }
}

const getVehicleLog = async (req, res) => {
    try {
    console.log({g:req.params})
        const post = await VehicleModel.find({ vehicle_number: req.params.vehicleNumber });
        res.json(post);
    } catch (err) {
        res.json({ message: err });
    }
}


router.get('/all', getPosts)
router.post('/createLog', createLog)
router.get('/single/:vehicleNumber', getVehicleLog)
export default router;

