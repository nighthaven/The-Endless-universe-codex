import {render, screen} from "@testing-library/react";
import ItemLayoutComponent from "./item-layout.component";
import {Provider} from "react-redux";
import configureStore from 'redux-mock-store';

const mockStore = configureStore([]);
const store = mockStore({
    item: {}
});

test("item layout component", () => {
    render(
        <Provider store={store}>
            <ItemLayoutComponent>
                <div>test content</div>
            </ItemLayoutComponent>
        </Provider>

    )
    const itemLayoutElement = screen.getByTestId("item-layout")
    expect(itemLayoutElement).toBeInTheDocument();
})