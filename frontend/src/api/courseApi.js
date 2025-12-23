import axios from "axios";

const API = "http://127.0.0.1:8000";

export const generateCourse = async (data) => {
  const res = await axios.post(`${API}/generate-course`, data);
  return res.data;
};

export const getJobStatus = async (jobId) => {
  const res = await axios.get(`${API}/status/${jobId}`);
  return res.data;
};
