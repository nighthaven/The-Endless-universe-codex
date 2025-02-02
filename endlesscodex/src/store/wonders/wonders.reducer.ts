import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

export const fetchWonders = createAsyncThunk(
  'wonders/fetchWonders',
  async () => {
    const response = await axios.get('/wonders');
    return response.data;
  }
);

interface Wonder {
  id: number;
  name: string;
  description: string;
  image: string;
}

const wondersReducer = createSlice({
  name: 'anomalies',
  initialState: {
    wonders: [] as Wonder[],
    loading: false,
    error: null as string | null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchWonders.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchWonders.fulfilled, (state, action) => {
        state.wonders = action.payload;
        state.loading = false;
      })
      .addCase(fetchWonders.rejected, (state) => {
        state.loading = false;
        state.error = 'Erreur lors de la récupération des anomalies.';
      });
  },
});

export default wondersReducer.reducer;
