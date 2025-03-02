package None;

import java.util.List;
import lombok.*;






/**
  An example.org test identifier.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ExampleIdentifier extends RelatedIdentifier {

  private String identifier;
  private String resolvingUrl;

}
