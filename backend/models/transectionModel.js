const mongoose = require("mongoose");

const transectionSchema = new mongoose.Schema(
  {
    amount: { type: Number, required: [true, "Amount is required"] },
    category: { type: String, required: [true, "Category is required"] },
    refrence: { type: String },
    description: { type: String, required: [true, "Description is required"] },
    date: { type: Date, required: [true, "Date is required"] },
  },
  { timestamps: true }
);

const transectionModel = mongoose.model("Transection", transectionSchema);

module.exports = transectionModel;
