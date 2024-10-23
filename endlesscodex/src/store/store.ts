import { configureStore } from '@reduxjs/toolkit';
import backgroundReducer from './background/background.reducer';
import itemLayoutReducer from "./item-layout/item-layout.reducer";
import anomaliesReducer from "./anomalies/anomalies.reducer";

const store = configureStore({
    reducer: {
        background: backgroundReducer,
        item: itemLayoutReducer,
        anomalies: anomaliesReducer,
    },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
