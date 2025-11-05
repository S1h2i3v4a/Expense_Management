const TransectionModel = require("../models/transectionModel");
const addTransection = async (req, res) => {
  try {
    const newTransection = new TransectionModel(req.body);
    await newTransection.save();
    res.status(201).json({
      success: true,
      message: "Transection added successfully",
      data: newTransection,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to add transection",
      error: error.message,
      console: console.log(error),
    });
  }
  console.log("Add transection called", req.body);
};

const getAllTransections = async (req, res) => {
  try {
    const transections = await TransectionModel.find({
      userId: req.body.userId,
    });
    res.status(200).json({
      success: true,
      message: "All transections fetched successfully",
      data: transections,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to fetch transections",
      error: error.message,
    });
  }
};

const getTransectionById = async (req, res) => {
  const { id } = req.params;
  try {
    const transection = await TransectionModel.findById(id);
    if (!transection) {
      return res.status(404).json({
        success: false,
        message: "Transection not found",
      });
    }
    res.status(200).json({
      success: true,
      message: "Transection fetched successfully",
      data: transection,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to fetch transection",
      error: error.message,
    });
  }
};

const updateTransection = async (req, res) => {
  const { id } = req.params;
  try {
    const transection = await TransectionModel.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    if (!transection) {
      return res.status(404).json({
        success: false,
        message: "Transection not found",
      });
    }
    res.status(200).json({
      success: true,
      message: "Transection updated successfully",
      data: transection,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to update transection",
      error: error.message,
    });
  }
};

const deleteTransection = async (req, res) => {
  const { id } = req.params;
  try {
    const transection = await TransectionModel.findByIdAndDelete(id);
    if (!transection) {
      return res.status(404).json({
        success: false,
        message: "Transection not found",
      });
    }
    res.status(200).json({
      success: true,
      message: "Transection deleted successfully",
      data: transection,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to delete transection",
      error: error.message,
    });
  }
};
module.exports = {
  addTransection,
  getAllTransections,
  getTransectionById,
  updateTransection,
  deleteTransection,
};
