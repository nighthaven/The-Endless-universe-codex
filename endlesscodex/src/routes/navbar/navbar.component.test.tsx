import {render, screen} from "@testing-library/react";
import NavbarComponent from "./navbar.component";
import { MemoryRouter } from "react-router-dom";

test("renders correctly", () => {
    render(
        <MemoryRouter>
            <NavbarComponent />
        </MemoryRouter>
    )
    const navigationElement = screen.getByTestId("navbar");
    expect(navigationElement).toBeInTheDocument();
})

