const express = require("express");

const {
  addTransection,
  getAllTransections,
  getTransectionById,
  updateTransection,
  deleteTransection,
} = require("../controllers/transectionCtrl");

const router = express.Router();

router.post("/add-transection", addTransection);
router.get("/get-all-transections", getAllTransections);
router.get("/get-transection/:id", getTransectionById);
router.put("/update-transection/:id", updateTransection);
router.delete("/delete-transection/:id", deleteTransection);

module.exports = router;
