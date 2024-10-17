import { createSlice } from '@reduxjs/toolkit';

const itemSlice = createSlice({
  name: 'item',
  initialState: {
    visible: false,
  },
  reducers: {
    showItem: (state) => {
      state.visible = true;
    },
    hideItem: (state) => {
      state.visible = false;
    },
  },
});

export const { showItem, hideItem } = itemSlice.actions;
export default itemSlice.reducer;
