package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  An example.org test identifier.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExampleIdentifier extends RelatedIdentifier {

  private String identifier;
  private String resolvingUrl;

}
