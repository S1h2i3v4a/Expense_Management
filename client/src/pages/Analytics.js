import React, { useState, useEffect } from "react";
import { Row, Col, Card, Progress, Select, Radio, message } from "antd";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from "chart.js";
import { Line, Bar, Pie } from "react-chartjs-2";
import Layout from "../components/Layout/Layout";
import axios from "axios";
import moment from "moment";

// Register ChartJS components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
);

const { Option } = Select;

function Analytics({ transactions: propTransactions = null }) {
  // fetchedTransactions: transactions loaded by this component when prop not provided
  const [fetchedTransactions, setFetchedTransactions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState("all");
  const [chartType, setChartType] = useState("bar");
  const [timeRange, setTimeRange] = useState("monthly");

  // Fetch transactions
  const getAllTransactions = async () => {
    try {
      setLoading(true);
      const { data } = await axios.get(
        "/api/v1/transections/get-all-transections"
      );
      setFetchedTransactions(data.data);
      setLoading(false);
    } catch (error) {
      message.error("Failed to fetch transactions");
      setLoading(false);
    }
  };

  // Only fetch when parent hasn't provided transactions via props
  useEffect(() => {
    if (!propTransactions) {
      getAllTransactions();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [propTransactions]);

  // Process data for analytics
  const processData = () => {
    const source = Array.isArray(propTransactions)
      ? propTransactions
      : fetchedTransactions;

    let filteredData = Array.isArray(source) ? [...source] : [];

    // Filter by category if not "all"
    if (selectedCategory !== "all") {
      filteredData = filteredData.filter(
        (t) => t.category === selectedCategory
      );
    }

    // Group by category
    const categoryTotals = filteredData.reduce((acc, t) => {
      acc[t.category] = (acc[t.category] || 0) + t.amount;
      return acc;
    }, {});

    // Time series data
    const timeSeriesData = filteredData.reduce((acc, t) => {
      const date = moment(t.date).format(
        timeRange === "monthly" ? "YYYY-MM" : "YYYY-MM-DD"
      );
      acc[date] = (acc[date] || 0) + t.amount;
      return acc;
    }, {});

    return {
      categoryTotals,
      timeSeriesData,
      totalAmount: filteredData.reduce((sum, t) => sum + (t.amount || 0), 0),
    };
  };

  const getChartData = () => {
    const { categoryTotals, timeSeriesData } = processData();
    const colors = [
      "#FF6B6B",
      "#4ECDC4",
      "#45B7D1",
      "#96CEB4",
      "#FFEEAD",
      "#D4A5A5",
      "#9B9B9B",
      "#A8E6CE",
      "#DCEDC2",
      "#FFD3B5",
    ];

    const baseConfig = {
      labels: Object.keys(
        chartType === "line" ? timeSeriesData : categoryTotals
      ),
      datasets: [
        {
          label:
            chartType === "line" ? "Amount Over Time" : "Amount by Category",
          data: Object.values(
            chartType === "line" ? timeSeriesData : categoryTotals
          ),
          backgroundColor: colors,
          borderColor: colors.map((c) => (chartType === "line" ? c : "white")),
          borderWidth: 1,
          tension: 0.1, // Smooth lines for line chart
        },
      ],
    };

    return baseConfig;
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "top",
        display: true,
      },
      title: {
        display: true,
        text: `Transaction Analytics - ${
          selectedCategory === "all" ? "All Categories" : selectedCategory
        }`,
      },
    },
    scales:
      chartType !== "pie"
        ? {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: "Amount ($)",
              },
            },
            x: {
              title: {
                display: true,
                text: chartType === "line" ? "Date" : "Category",
              },
            },
          }
        : undefined,
  };

  const renderChart = () => {
    const data = getChartData();

    switch (chartType) {
      case "line":
        return <Line data={data} options={chartOptions} />;
      case "bar":
        return <Bar data={data} options={chartOptions} />;
      case "pie":
        return <Pie data={data} options={chartOptions} />;
      default:
        return null;
    }
  };

  const renderProgressBars = () => {
    const { categoryTotals, totalAmount } = processData();

    return Object.entries(categoryTotals).map(([category, amount]) => (
      <Col span={8} key={category} className="mb-4">
        <Card>
          <h5>{category.toUpperCase()}</h5>
          <Progress
            type="circle"
            percent={Math.round((amount / totalAmount) * 100)}
            format={(percent) => `${percent}%\n$${amount.toFixed(2)}`}
          />
        </Card>
      </Col>
    ));
  };

  const content = (
    <div className="container mt-4">
      <h2 className="mb-4">Analytics Dashboard</h2>

      {/* Controls */}
      <Row gutter={[16, 16]} className="mb-4">
        <Col span={8}>
          <Select
            value={selectedCategory}
            onChange={setSelectedCategory}
            style={{ width: "100%" }}
          >
            <Option value="all">All Categories</Option>
            <Option value="income">Income</Option>
            <Option value="expense">Expense</Option>
            <Option value="salary">Salary</Option>
            <Option value="food">Food</Option>
            <Option value="entertainment">Entertainment</Option>
            <Option value="travel">Travel</Option>
            <Option value="other">Other</Option>
          </Select>
        </Col>

        <Col span={8}>
          <Radio.Group
            value={chartType}
            onChange={(e) => setChartType(e.target.value)}
          >
            <Radio.Button value="bar">Bar</Radio.Button>
            <Radio.Button value="line">Line</Radio.Button>
            <Radio.Button value="pie">Pie</Radio.Button>
          </Radio.Group>
        </Col>

        <Col span={8}>
          <Radio.Group
            value={timeRange}
            onChange={(e) => setTimeRange(e.target.value)}
          >
            <Radio.Button value="daily">Daily</Radio.Button>
            <Radio.Button value="monthly">Monthly</Radio.Button>
          </Radio.Group>
        </Col>
      </Row>

      {/* Charts */}
      <Card className="mb-4">
        <div style={{ height: "400px" }}>{renderChart()}</div>
      </Card>

      {/* Progress Circles */}
      <h3 className="mb-3">Category Distribution</h3>
      <Row gutter={[16, 16]}>{renderProgressBars()}</Row>
    </div>
  );

  // If parent passed transactions (embedded in HomePage), don't render Layout wrapper
  if (propTransactions) {
    return content;
  }

  return <Layout>{content}</Layout>;
}

export default Analytics;
