import {render, screen} from '@testing-library/react';
import AboutContentComponent from "./about-content.component";
import configureStore from 'redux-mock-store';
import {Provider} from "react-redux";
import aboutImage from "../../img/about.png";

const mockStore = configureStore();
const store = mockStore({
    background: {},
    item: {},
});


test('renders about content', () => {
    render(
        <Provider store={store}>
            <AboutContentComponent/>
        </Provider>
    )
    const aboutContentElement = screen.getByTestId("about")
    expect(aboutContentElement).toBeInTheDocument();

    const itemImageElements = screen.getAllByTestId("item-layout")
    expect(itemImageElements.length).toEqual(2)

    const imageElement = screen.getByRole('img');
    expect(imageElement).toHaveAttribute('src', aboutImage);

    const textElement = screen.getByText(/My name is Boris, I am a developer/i)
    expect(textElement).toBeInTheDocument();
})
