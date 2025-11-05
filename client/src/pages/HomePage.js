import React, { useState, useEffect } from "react";
import Layout from "./../components/Layout/Layout";
import axios from "axios";
import {
  Modal,
  Form,
  Input,
  Select,
  DatePicker,
  Table,
  message,
  Switch,
  Tooltip,
} from "antd";
import moment from "moment";
import Analytics from "./Analytics";
import { TableOutlined, AreaChartOutlined } from "@ant-design/icons";

// Configure axios defaults
axios.defaults.baseURL = "http://localhost:8080";

// Add styles for view transitions
const styles = {
  viewSwitch: {
    transition: "all 0.3s ease",
    "&:hover": {
      transform: "scale(1.1)",
    },
  },
  analyticsContainer: {
    opacity: 1,
    transition: "opacity 0.3s ease-in-out",
  },
};

const { Option } = Select;

const HomePage = () => {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [editing, setEditing] = useState(null);
  const [form] = Form.useForm();
  const [filterCategory, setFilterCategory] = useState("all");
  const [sortBy, setSortBy] = useState("date");
  const [sortOrder, setSortOrder] = useState("desc");
  const [view, setView] = useState("table");

  // Fetch all transactions
  const getAllTransactions = async () => {
    try {
      setLoading(true);
      const { data } = await axios.get(
        "/api/v1/transections/get-all-transections"
      );
      setTransactions(data.data);
      setLoading(false);
    } catch (error) {
      message.error("Failed to fetch transactions");
      setLoading(false);
    }
  };

  useEffect(() => {
    getAllTransactions();
  }, []);

  // derive displayed transactions with filter and sort
  const getDisplayedTransactions = () => {
    try {
      let list = Array.isArray(transactions) ? [...transactions] : [];

      // filter by category
      if (filterCategory && filterCategory !== "all") {
        list = list.filter((t) => t.category === filterCategory);
      }

      // sort
      list.sort((a, b) => {
        if (sortBy === "date") {
          const da = a?.date ? new Date(a.date).getTime() : 0;
          const db = b?.date ? new Date(b.date).getTime() : 0;
          return sortOrder === "asc" ? da - db : db - da;
        }

        if (sortBy === "amount") {
          const aa = Number(a?.amount) || 0;
          const ab = Number(b?.amount) || 0;
          return sortOrder === "asc" ? aa - ab : ab - aa;
        }

        return 0;
      });

      return list;
    } catch (err) {
      return transactions;
    }
  };

  // Handle form submission
  const handleSubmit = async (values) => {
    try {
      setLoading(true);
      const payload = {
        ...values,
        date: values.date.toDate(),
      };

      if (editing) {
        await axios.put(
          `/api/v1/transections/update-transection/${editing._id}`,
          payload
        );
        message.success("Transaction updated successfully");
      } else {
        await axios.post("/api/v1/transections/add-transection", payload);
        message.success("Transaction added successfully");
      }

      setShowModal(false);
      form.resetFields();
      setEditing(null);
      getAllTransactions();
      setLoading(false);
    } catch (error) {
      message.error("Error occurred while saving");
      setLoading(false);
    }
  };

  // Handle delete
  const handleDelete = async (id) => {
    try {
      setLoading(true);
      await axios.delete(`/api/v1/transections/delete-transection/${id}`);
      message.success("Transaction deleted successfully");
      getAllTransactions();
    } catch (error) {
      message.error("Error deleting transaction");
      setLoading(false);
    }
  };

  // Table columns configuration
  const columns = [
    {
      title: "Date",
      dataIndex: "date",
      render: (text) => moment(text).format("YYYY-MM-DD"),
    },
    {
      title: "Amount",
      dataIndex: "amount",
    },
    {
      title: "Category",
      dataIndex: "category",
    },
    {
      title: "Reference",
      dataIndex: "refrence",
    },
    {
      title: "Description",
      dataIndex: "description",
    },
    {
      title: "Actions",
      render: (_, record) => (
        <>
          <button
            className="btn btn-sm btn-primary mx-2"
            onClick={() => {
              setEditing(record);
              setShowModal(true);
              form.setFieldsValue({
                ...record,
                date: moment(record.date),
              });
            }}
          >
            Edit
          </button>
          <button
            className="btn btn-sm btn-danger"
            onClick={() => handleDelete(record._id)}
          >
            Delete
          </button>
        </>
      ),
    },
  ];

  return (
    <Layout>
      <div className="container mt-4">
        <div className="d-flex justify-content-between align-items-center mb-4">
          <div className="d-flex align-items-center">
            <h2 className="mb-0 me-4">
              Transactions {view === "table" ? "List" : "Analytics"}
            </h2>
            <Tooltip
              title={`Switch to ${
                view === "table" ? "Analytics" : "Table"
              } View`}
            >
              <Switch
                checked={view === "table"}
                onChange={(checked) => setView(checked ? "table" : "analytics")}
                checkedChildren={<TableOutlined />}
                unCheckedChildren={<AreaChartOutlined />}
                className="me-2"
              />
            </Tooltip>
          </div>
          <button
            className="btn btn-primary"
            onClick={() => {
              setShowModal(true);
              setEditing(null);
              form.resetFields();
            }}
          >
            Add New Transaction
          </button>
        </div>

        {view === "table" ? (
          <>
            {/* Filter & Sort controls */}
            <div className="d-flex align-items-center mb-3 gap-2">
              <div>
                <label className="me-2">Category:</label>
                <Select
                  value={filterCategory}
                  onChange={(val) => setFilterCategory(val)}
                  style={{ width: 160 }}
                >
                  <Option value="all">All</Option>
                  <Option value="income">Income</Option>
                  <Option value="expense">Expense</Option>
                  <Option value="salary">Salary</Option>
                  <Option value="food">Food</Option>
                  <Option value="entertainment">Entertainment</Option>
                  <Option value="travel">Travel</Option>
                  <Option value="other">Other</Option>
                </Select>
              </div>

              <div>
                <label className="me-2">Sort by:</label>
                <Select
                  value={sortBy}
                  onChange={(val) => setSortBy(val)}
                  style={{ width: 140 }}
                >
                  <Option value="date">Date</Option>
                  <Option value="amount">Amount</Option>
                </Select>
              </div>

              <div>
                <label className="me-2">Order:</label>
                <Select
                  value={sortOrder}
                  onChange={(val) => setSortOrder(val)}
                  style={{ width: 120 }}
                >
                  <Option value="desc">Newest / High to Low</Option>
                  <Option value="asc">Oldest / Low to High</Option>
                </Select>
              </div>
            </div>

            <Table
              columns={columns}
              dataSource={getDisplayedTransactions()}
              loading={loading}
              rowKey="_id"
            />
          </>
        ) : (
          <div className="analytics-container" style={{ marginTop: "-16px" }}>
            <Analytics />
          </div>
        )}

        <Modal
          title={editing ? "Edit Transaction" : "Add New Transaction"}
          open={showModal}
          onCancel={() => {
            setShowModal(false);
            setEditing(null);
            form.resetFields();
          }}
          footer={null}
        >
          <Form form={form} layout="vertical" onFinish={handleSubmit}>
            <Form.Item
              name="amount"
              label="Amount"
              rules={[{ required: true, message: "Please enter amount" }]}
            >
              <Input type="number" />
            </Form.Item>

            <Form.Item
              name="category"
              label="Category"
              rules={[{ required: true, message: "Please select category" }]}
            >
              <Select>
                <Option value="income">Income</Option>
                <Option value="expense">Expense</Option>
                <Option value="salary">Salary</Option>
                <Option value="food">Food</Option>
                <Option value="entertainment">Entertainment</Option>
                <Option value="travel">Travel</Option>
                <Option value="other">Other</Option>
              </Select>
            </Form.Item>

            <Form.Item name="refrence" label="Reference">
              <Input />
            </Form.Item>

            <Form.Item
              name="description"
              label="Description"
              rules={[{ required: true, message: "Please enter description" }]}
            >
              <Input.TextArea />
            </Form.Item>

            <Form.Item
              name="date"
              label="Date"
              rules={[{ required: true, message: "Please select date" }]}
            >
              <DatePicker className="w-100" />
            </Form.Item>

            <div className="d-flex justify-content-end">
              <button type="submit" className="btn btn-primary">
                {editing ? "Update" : "Add"} Transaction
              </button>
            </div>
          </Form>
        </Modal>
      </div>
    </Layout>
  );
};

export default HomePage;
