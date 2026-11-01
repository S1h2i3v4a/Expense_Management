const mongoose = require("mongoose");
const colors = require("colors");

const connectDb = async () => {
  try {
    const mongoURI = process.env.MONGO_URL || process.env.MONGODB_URI;
    if (!mongoURI) {
      console.log("⚠️ Warning: MONGO_URL or MONGODB_URI is not set in environment variables!".yellow);
      return;
    }
    await mongoose.connect(mongoURI, {
      serverSelectionTimeoutMS: 5000,
    });
    console.log(`Server Running On ${mongoose.connection.host}`.bgCyan.white);
  } catch (error) {
    console.log(`MongoDB connection error: ${error.message || error}`.bgRed);
  }
};

module.exports = connectDb;
