import router from "./controller.js";

import mongoose from "mongoose";
const { Schema } = mongoose;

const vehicleSchema = new Schema({
    vehicle_number: {
        type: String,
        required: true
    },
    time: {
        type: Date,
        required: true
    },
    location:{
       type:String,
       required: true
    }
});

const VehicleModel = mongoose.model('junction1', vehicleSchema);

export default VehicleModel;
// module.exports = VehicleModel;
