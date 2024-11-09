import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchAnomalies = createAsyncThunk(
  'anomalies/fetchAnomalies',
  async () => {
    const response = await axios.get('/anomalies');
    return response.data;
  }
);

interface Anomaly {
  id: number;
  name: string;
  description: string;
  image: string;
}

const anomaliesReducer = createSlice({
  name: 'anomalies',
  initialState: {
    anomalies: [] as Anomaly[],
    loading: false,
    error: null as string | null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAnomalies.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAnomalies.fulfilled, (state, action) => {
        state.anomalies = action.payload;
        state.loading = false;
      })
      .addCase(fetchAnomalies.rejected, (state) => {
        state.loading = false;
        state.error = 'Erreur lors de la récupération des anomalies.';
      });
  },
});

export default anomaliesReducer.reducer;
